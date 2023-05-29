def schedule_jobs(jobs):
    sorted_jobs = sorted(jobs, key=lambda x: x[1])  # Sort jobs based on their end time
    scheduled_jobs = [sorted_jobs[0]]  # Schedule the first job
    
    for job in sorted_jobs[1:]:
        if job[0] >= scheduled_jobs[-1][1]:  # If the start time of the job is after the end time of the last scheduled job
            scheduled_jobs.append(job)  # Schedule the job
            
    return scheduled_jobs


# Prompt user for job input
num_jobs = int(input("Enter the number of jobs: "))
jobs = []
for i in range(num_jobs):
    job_name = input(f"Enter the name of job {i + 1}: ")
    start_time = int(input(f"Enter the start time of job {i + 1}: "))
    end_time = int(input(f"Enter the end time of job {i + 1}: "))
    jobs.append((job_name, start_time, end_time))

# Schedule jobs
scheduled_jobs = schedule_jobs(jobs)

# Print scheduled jobs
print("Scheduled Jobs:")
for job in scheduled_jobs:
    print(f"Job: {job[0]}, Start Time: {job[1]}, End Time: {job[2]}")
