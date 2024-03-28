# Example 1

In this scenario, our objective is to conduct a straightforward machine learning training task on a single GPU through an interactive job submission. We will employ the ResNet-18 model along with the CIFAR-10 dataset for this purpose.


## Steps

1. **Login to the HPC system**: Please login to the HPC system using your credentials.

```bash
ssh <username>@login.rc.fas.harvard.edu
```

2. **Configuring Your Development Environment**: There are several approaches to setting up your environment, including Docker, Conda, or module systems. For comprehensive instructions, please refer to the handbook. To streamline this demonstration, we'll employ the PyTorch Docker image through Singularity. You're presented with two options:

    - **Option 1**: Pull the PyTorch Docker image from Docker Hub.

    ```bash
    singularity pull docker://pytorch/pytorch_2.1.2-cuda12.1-cudnn8-runtime
    ```
    This will generate a Singularity image file named `pytorch_pytorch_2.1.2-cuda12.1-cudnn8-runtime.sif`.

    - **Option 2**: Use the image from the shared scratch space.

    ```bash
    CONTAINER=/n/holyscratch01/kempner_dev/Shared/intro_compute_march_2024/pytorch_2.1.2-cuda12.1-cudnn8-runtime.sif
    ```
Should you choose Option 1, it's necessary to allocate a compute node due to the potential time required to download the image; performing this operation on the login node is generally not advisable. A GPU node is not required for this task—any readily available, basic partition should suffice. On the other hand, Option 2 is quicker and provides access to the same image without the wait.

3. **Repository Cloning**: Copy the repository into the scratch space.

First, change directories to your lab's scratch space with `cd $SCRATCH`. Create a personal directory within this space and move into it. After that, proceed to clone the repository.

```bash
git clone https://github.com/KempnerInstitute/intro-compute-march-2024.git
```
After cloning the repository, navigate to the Example_1 directory.

4. **Allocating Resources**: We will request an interactive session to execute our training task. We will utilize the `salloc` command to request a single GPU, as shown below.

```bash 
salloc --partition=<your desired partition> --nodes=1 --ntasks-per-node=1 --cpus-per-task=16 --gres=gpu:1 --mem=250G --time=4:00:00  --account=<your fairshare account> --constraint=a100
```

This command will allocate a single GPU node with 16 CPUs, 250GB of memory, and a time limit of 4 hours. The `--account` flag should be replaced with your fairshare account. The `--constraint` flag specifies the GPU type; in this case, it's an A100. The `--partition` flag designates the partition you wish to use.

5. **Running the Training Task**: Execute the training script.

```bash
singularity exec --nv pytorch_2.1.2-cuda12.1-cudnn8-runtime.sif python train_cifer10_resnet.py --batch_size 128 --epoch 50 --lr 0.01 --model resnet18
```

This command will run the training script with the specified parameters. The `--nv` flag is necessary to enable GPU support within the Singularity container. The `--batch_size`, `--epoch`, `--lr`, and `--model` flags are used to set the batch size, number of epochs, learning rate, and model type, respectively.

For the first time, the code will download the CIFAR-10 dataset. Subsequent runs will utilize the cached dataset.

6. **Monitoring the Training Task**: You can monitor the training task by checking the output in the terminal, and monitoring the GPU and CPU usage. 

- Pick the compute node. For example, in `jharvard@holygpu8a19103`, `holygpu8a19103` is the compute node name.
- Open a new terminal and SSH into the login node.
- Then run:

```bash
ssh <comppute node>
```
- Run the following command to monitor the GPU usage:

```bash
nvtop
```

- Run the following command to monitor the CPU usage:

```bash
htop
```

7. **Deallocating Resources**: Once the training task is complete, you can deallocate the resources by exiting the interactive session.

```bash
exit
```