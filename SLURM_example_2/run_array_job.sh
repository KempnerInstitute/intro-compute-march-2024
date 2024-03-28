#! /bin/bash
#SBATCH --job-name=job-array
#SBATCH --account=            <------ Add fair share account (e.g., kempner_grad)
#SBATCH --output=%A_%a.out
#SBATCH --nodes=1           
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1 
#SBATCH --cpus-per-task=1
#SBATCH --time=10:00
#SBATCH --mem=4GB
#SBATCH --partition=kempner_requeue
#SBATCH --array=1-4%2

module load python

python hyperparameter_tuning.py --task_id $SLURM_ARRAY_TASK_ID