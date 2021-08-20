def roundRobin(jobs, slice, index):
    (i, res, jobs) = (0, 0, jobs[:])
    while jobs[index]:
        res += min(slice, jobs[i])
        jobs[i] = max(0, jobs[i] - slice)
        i = (i + 1) % len(jobs)
    return res
