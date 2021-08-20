def SJF(jobs, index):
    job = jobs[index]
    return sum(sorted(jobs)[:sorted(jobs).index(job) + 1]) + job * jobs[:index].count(job)
