def SJF(jobs, index):
    return sum(c for i, c in enumerate(jobs) if c < jobs[index] or (c == jobs[index] and i <= index))
