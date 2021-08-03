def roundRobin(jobs, slice, index):
    cc = i = 0
    while jobs[index] > 0:
        cc += min(slice, jobs[i])
        jobs[i] = max(0, jobs[i] - slice)
        i = (i + 1) % len(jobs)
    return cc
