# Example 3

In this scenario, our objective is to learn how to submit a batch job array to 
conduct a hyperparameter tuning. We will employ the ResNet-18 model along with the CIFAR-10 dataset for this purpose. We will also integrate weights and biases (wandb.ai) to monitor the training process. Another option is to use the `sweep` feature in wandb.ai to conduct the hyperparameter tuning, which is not covered in this example.

## Steps

1. **Open an account on Weights & Biases**: Please create an account on [Weights & Biases](https://wandb.ai/). This platform will be used to monitor the training process.

After creating an account and starting a project, you will be provided with an access key. This key will be used to authenticate your training script with the Weights & Biases platform.

- Open the `.netrc` file in your home directory.
- Add the following line to the file, replacing `<account email>` with your Weights & Biases email and `<api_key>` with your access key.

```bash
machine api.wandb.ai 
  login <account email> 
  password <api key>
```

2. **Login to the HPC system**: Please login to the HPC system using your credentials.

```bash
ssh <username>@login.rc.fas.harvard.edu
```

3. **Configuring Your Development Environment**: There are several approaches to setting up your environment, including Docker, Conda, or module systems. For comprehensive instructions, please refer to the handbook. To streamline this demonstration, we'll employ the PyTorch Docker image through Singularity.

The original PyTorch Docker image does not include the `wandb` library. We need to modify the image to include this library.

**Note**: This step is very time consuming. For the workshop, please use the available image that is already modified. The modified image is available in the shared scratch space. You can use this image to run the training script.

```bash
CONTAINER=/n/holyscratch01/kempner_dev/Shared/intro_compute_march_2024/pytorch_2.1.2-cuda12.1-cudnn8-runtime_wandb.sif
```
4. **Repository Cloning**: Copy the repository into the scratch space.

First, change directories to your lab's scratch space with `cd $SCRATCH`. Create a personal directory within this space and move into it. After that, proceed to clone the repository.

```bash
git clone https://github.com/KempnerInstitute/intro-compute-march-2024.git
```

After cloning the repository, navigate to the Example_3 directory.

5. **Reviewing the batch script**: The batch script `run.sh` is provided in the `Example_2` directory. This script contains the necessary commands to execute the training task. You can review the script to understand the parameters and configurations. You also need to modify the script to include your fairshare account. 

After updating the script, you can submit the job using the following command:

```bash
sbatch run.sh
```

6. **Monitoring the Training Task**: You can monitor the training task by checking your weights and biases dashboard. The dashboard will provide real-time updates on the training process, including metrics, graphs, and other relevant information.

7. Done!



