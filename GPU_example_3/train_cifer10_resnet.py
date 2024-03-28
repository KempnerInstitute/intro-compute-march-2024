import os
import logging
import argparse


import wandb
import torch
import torchvision
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms



# set torch_home to a cache directory ------------------------------------------
cache_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cache')
os.environ['TORCH_HOME'] = cache_path
os.makedirs(cache_path, exist_ok=True)
os.makedirs(os.path.join(cache_path, 'checkpoints'), exist_ok=True)


def train_one_epoch(model, loader, optimizer, device):
    """
    Train the model for one epoch

    Args:
        model: the model to train
        loader: the training data loader
        optimizer: the optimizer to use
        device: the device to train on (CPU or GPU)
    """
    model.train()
    total_loss = 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        output = model(images)
        loss = torch.nn.functional.cross_entropy(output, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    avg_loss = total_loss / len(loader)
    logging.info(f"Training Loss: {avg_loss}")
    wandb.log({"training_loss": avg_loss})

def validate(model, loader, device):
    """
    Validate the model

    Args:
        model: the model to validate
        loader: the validation data loader
        device: the device to validate on (CPU or GPU)
    """
    model.eval()
    total_loss = 0
    correct = 0
    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)
            output = model(images)
            loss = torch.nn.functional.cross_entropy(output, labels)
            total_loss += loss.item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(labels.view_as(pred)).sum().item()
    avg_loss = total_loss / len(loader)
    accuracy = 100. * correct / len(loader.dataset)
    logging.info(f'Validation Loss: {avg_loss}, Accuracy: {accuracy}%')
    wandb.log({"validation_loss": avg_loss, "validation_acc": accuracy})

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Train and validate a model on CIFAR-10')
    parser.add_argument('--batch_size', 
                        type=int, 
                        default=256, 
                        help='batch size')
    parser.add_argument('--epochs', 
                        type=int, 
                        default=50, 
                        help='number of epochs')
    parser.add_argument('--lr', 
                        type=float, 
                        default=0.01, 
                        help='learning rate')
    parser.add_argument('--model', 
                        type=str, 
                        default='resnet18', 
                        help='Resnet model to use')
    return parser.parse_args()

def save_checkpoint(state, filename="checkpoint.pth.tar"):
    torch.save(state, filename)
    logging.info(f"Checkpoints saved to {filename}")

def main():
    if torch.cuda.is_available():
        device = torch.device('cuda')
    else:
        logging.warning('No GPU found, using CPU')
        device = torch.device('cpu')
    args = parse_args()

    wandb.init(
        project=args.wandb_pr_name,
        config={
            "learning_rate":args.lr,
            "epochs":args.epochs,
            "batch_size": args.batch_size,
            }
        )

    preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                             std=[0.229, 0.224, 0.225]),
    ])

    # Load training and validation datasets
    train_dataset = datasets.CIFAR10(root='./data', 
                                     train=True, 
                                     download=True, 
                                     transform=preprocess)
    validate_dataset = datasets.CIFAR10(root='./data', 
                                        train=False, 
                                        download=True, 
                                        transform=preprocess)

    train_loader = DataLoader(train_dataset, 
                              batch_size=args.batch_size, 
                              shuffle=True, 
                              num_workers=4, 
                              pin_memory=True)
    
    validate_loader = DataLoader(validate_dataset, 
                                 batch_size=args.batch_size, 
                                 shuffle=False, 
                                 num_workers=4, 
                                 pin_memory=True)

    if args.model == "resnet50":
        model = torchvision.models.resnet50(
            weights=torchvision.models.ResNet50_Weights.DEFAULT)
    elif args.model == "resnet18":
        model = torchvision.models.resnet18(
            weights=torchvision.models.ResNet18_Weights.DEFAULT)
    else:
        raise ValueError("model should be either resnet50 or resnet18")

    model.conv1 = nn.Conv2d(3, 64, 
                            kernel_size=3, stride=1, padding=1, bias=False)
    model.fc = nn.Linear(model.fc.in_features, 10)
    model.to(device)

    optimizer = torch.optim.SGD(model.parameters(), 
                                lr=args.lr, momentum=0.9, weight_decay=5e-4)

    for epoch in range(args.epochs):
        logging.info(f"Epoch {epoch+1}/{args.epochs}")
        train_one_epoch(model, train_loader, optimizer, device)
        validate(model, validate_loader, device)

        # save a checkpoint
        checkpoint_filename = (f"{cache_path}/checkpoints/"
                               f"checkpoint_epoch_{epoch+1}.pth.tar")
        save_checkpoint({
            'epoch': epoch + 1,
            'state_dict': model.state_dict(),
            'optimizer': optimizer.state_dict(),
            }, filename = checkpoint_filename)
    wandb.finish()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
