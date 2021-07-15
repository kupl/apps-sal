SJF = lambda jobs, index: sum(j for i, j in enumerate(jobs) if j < jobs[index] or (j == jobs[index] and i < index)) + jobs[index]
