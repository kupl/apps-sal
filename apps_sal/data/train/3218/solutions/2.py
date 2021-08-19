def SJF(jobs, index):
    return sum((n for (i, n) in enumerate(jobs) if n < jobs[index] or (n == jobs[index] and i <= index)))
