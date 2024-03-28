# SLURM Useful Commands

Slurm offers a diverse set of commands, each designed to fulfill specific tasks, often with the aid of various options and flags. 

In order to use the commands effectively lets submit a dummy job to the cluster. 

## Steps

1. **Login to the HPC system**: Please login to the HPC system using your credentials.

```bash
ssh <username>@login.rc.fas.harvard.edu
```

2. **Navigate to the scratch space**: Change directories to your lab's scratch space with `cd $SCRATCH` and create a folder for the workshop excercise and navigate to it.

3. **Clone the repository**: Clone the repository.

```bash
git clone https://github.com/KempnerInstitute/intro-compute-march-2024.git
```

After cloning the repository, navigate to the `SLURM_example_1` directory.

Here we have a python script that is simply occupying the CPU and Memory for a certain amount of time. Take a look at the job submission script `run.sh` and the python script `cpu_mem_occupy.py`.

4. **Test the job submission script**: 

You can test the job submission by adding the following command to the `run.sh` script:

```bash
#SBATCH --test-only
```

This will tell you what would happen if you submit the job without actually submitting it. (Try it!)

5. **Submit the job**: 

Drop the `--test-only` flag and set the duration to 300 seconds and submit the job using the following command:

```bash
sbatch run.sh
```

6. **Check the job status**:

You can check the status of the job using the following command:

```bash
squeue -u <username> 
```
or 

```bash
squeue -u $USER
```
or 

```bash
squeue --me
```

Note that the wrapper squeue command has some delay in updating the status of the job.

7. **Check efficiency of the job**:

You can check the efficiency of the job using the following command:

```bash
seff <job_id>
```
This will provide you with the CPU and Memory efficiency of the job. Try different values and see if you can run the job out of memory or CPU.

8. **Cancel the job**:

Resubmit the job and try to cancel the job using the following commands.

- Cancel the job using the job id:

    ```bash
    scancel <job_id>
    ```
- Cancel all jobs of the user:

    ```bash
    scancel -u <username>
    ```
- Cancel only pending jobs:

    ```bash
    scancel --state=pending -u <username>
    ```


9. **Hold and Release the job**:

If you have submitted the job and want to hold it for some reason (e.g., you releazied that there is a problem in the input data), you can put the job on hold. This will prevent the job from running until you release it and will increase the priority of the job.

```bash
scontrol hold <job_id>
```
After fixing the issue, you can release the job using the following command:

```bash
scontrol release <job_id>
```

10. **Fairshare Accounts**:

You can check the fairshare accounts using the following command:

```bash
sacctmgr show associations user=<user_id> format=account%30
```
You can also check who belongs to a specific account:

```bash
sacctmgr show associations account=<account_name>
```

Check fairshare value for your account:

```bash
sshare --account=<account_name>
```
You can also see a summary of the effectiveness of the jobs that you have run with each account using the following command:

```bash
seff-account --account=<account_id> 
```

You can use `scalc` command to calculate different fairshare-related values. First let's take a look at the labs fairshare value:

```bash
sshare -a --format=Account,FairShare
```
Pick a lab account and use the following command to calculate the fairshare value:

```bash
scalc
``` 
Choose, option 3, and provide the requested information.


11. **Report the Usage**:

`sreport` is a powerful command to provide a summary of different aspects of the cluster usage. See, from your group, who used the cluster the most in the last 7 days

```bash
sreport cluster AccountUtilizationByUser account=<account_name> Start=2024-03-21 End=2024-03-28
```



