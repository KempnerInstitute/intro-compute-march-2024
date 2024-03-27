#! /bin/bash
#SBATCH --job-name=resnet
#SBATCH --time=0-02:00:00
#SBATCH --partition=              # <---- Add partition name (e.g., kempner)
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=250G
#SBATCH --output=resnet_%J.out
#SBATCH --error=resnet_%J.err  
#SBATCH --account=                # <---- Add fair share account (e.g., kempner_grad)
#SBATCH --gres=gpu:1



CONTAINER_PATH= # <---- Add path to container 
RUNNING_SOURCE= # <---- Add path to running source code
WANDB_PR_NAME= # <---- Add wandb project name 


srun singularity exec --nv $CONTAINER_PATH python train_cifer10_resnet18.py --batch_size 64 --epoch 40 --lr 0.01 --model resnet18 --wandb_pr_name $WANDB_PR_NAME