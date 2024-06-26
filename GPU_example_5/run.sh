#! /bin/bash
#SBATCH --job-name=resnet_lightning
#SBATCH --time=0-01:00:00
#SBATCH --partition=                  # <---- Add partition name (e.g., kempner)
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=4
#SBATCH --mem=1000G
#SBATCH --output=resnet_lightning.out
#SBATCH --error=resnet_lightning.err
#SBATCH --account=                    # <---- Add fair share account (e.g., kempner_grad)
#SBATCH --gres=gpu:4



MODEL="resnet50"
BATCH_SIZE=64


DATADIR=/n/holyscratch01/kempner_dev/Shared/intro_compute_march_2024/imagenet_winter21_subset           
CONTAINER_PATH=CONTAINER=/n/holyscratch01/kempner_dev/Shared/intro_compute_march_2024/pytorch_2.1.2-cuda12.1-cudnn8-runtime-lightning.sif

time srun singularity exec 
     --bind $DATADIR \ 
     --nv $CONTAINER_PATH python3 train_imagenet_resnet.py \
     --dataset $DATADIR \
     --epochs 10 \
     --batch_size $BATCH_SIZE \
     --num_workers $SLURM_CPUS_PER_TASK \
     --num_gpus $SLURM_GPUS_ON_NODE \
     --num_nodes $SLURM_NNODES \
     --model $MODEL

