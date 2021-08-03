def roundRobin(jobs, slice, index):
    q = (jobs[index] - 1) // slice
    return (
        sum(min(x, (q + 1) * slice) for x in jobs[:index + 1]) +
        sum(min(x, q * slice) for x in jobs[index + 1:])
    )
