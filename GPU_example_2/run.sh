#! /bin/bash
#SBATCH --job-name=resnet
#SBATCH --time=0-02:00:00
#SBATCH --partition=              # <---- Add partition name (e.g., kempner)
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=          # <---- Add number of cpus (e.g., 16)
#SBATCH --mem=                    # <---- Add memory (e.g., 250G)
#SBATCH --output=resnet_%J.out
#SBATCH --error=resnet_%J.err  
#SBATCH --account=                # <---- Add fair share account (e.g., kempner_grad)
#SBATCH --gres=gpu:1



CONTAINER_PATH= # <---- Add path to container 
RUNNING_SOURCE= # <---- Add path to running source code
WANDB_PR_NAME= # <---- Add wandb project name 

BATCH_SIZE=64
LR=0.01
EPOCH=40
MODEL=resnet18



srun singularity exec --nv $CONTAINER_PATH \
     python train_cifer10_resnet18.py \
     --batch_size $BATCH_SIZE \
     --epoch $EPOCH \
     --lr $LR \
     --model $MODEL \
     --wandb_pr_name $WANDB_PR_NAME