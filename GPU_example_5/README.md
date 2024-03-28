# Example 5

In this scenario, our objective is to learn how to submit a batch job to train a model on 8 GPUs on two nodes. We will use the pytorchlightening to distribute the model across the GPUs. We will employ the ResNet-50 model along with the subset of imagenet dataset for this purpose. 

## Steps

1. **Login to the HPC system**: Please login to the HPC system using your credentials.

```bash
ssh <username>@login.rc.fas.harvard.edu
```

2. **Configuring Your Development Environment**: There are several approaches to setting up your environment, including Docker, Conda, or module systems. For comprehensive instructions, please refer to the handbook. To streamline this demonstration, we'll employ the PyTorch Docker image through Singularity.

Note that the original PyTorch Docker image does not include the `lightning` library. We need to modify the image to include this library. The process is similar to the one we followed in the previous examples. For this workshop session, we have already modified the image to include the `lightning` library. You can use the available image to run the training script.

```bash
CONTAINER=TBD
```

3. **Repository Cloning**: Copy the repository into the scratch space.

First, change directories to your lab's scratch space with `cd $SCRATCH`. Create a personal directory within this space and move into it. After that, proceed to clone the repository.

```bash
TBD
```

After cloning the repository, navigate to the Example_5 directory.

4. **Reviewing the batch script**: The batch script `run.sh` is provided in the `Example_5` directory. This script contains the necessary commands to execute the training task. You can review the script to understand the parameters and configurations. You also need to modify the script to include your fairshare account.

