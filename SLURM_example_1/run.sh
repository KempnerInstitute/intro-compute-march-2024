#! /bin/bash
#SBATCH --job-name=cpu_mem_occupy
#SBATCH --time=0-01:00:00
#SBATCH --partition=test     
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --output=sleep_%J.out
#SBATCH --error=sleep_%J.err  
#SBATCH --account=               <------ Add fair share account (e.g., kempner_grad)


DURATION=60
CPU_M_SIZE=100
CPU_M_FREQ=100
MEM_M_SIZE=1000
MEM_M_FREQ=400


module load python/3.10.13-fasrc01

python  cpu_mem_occupy.py  --duration $DURATION --cpu_m_size $CPU_M_SIZE  --cpu_m_freq $CPU_M_FREQ  --mem_m_size $MEM_M_SIZE  --mem_m_freq $MEM_M_FREQ 