SJF = lambda jobs, index: sum(j for i, j in enumerate(jobs) if j <= jobs[index] and (jobs[i] != jobs[index] or i <= index))
