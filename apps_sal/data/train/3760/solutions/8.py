def roundRobin(jobs, limit, target):
    queue = list(enumerate(jobs))
    cycles = 0
    while True:
        (index, job) = queue.pop(0)
        if limit >= job:
            cycles += job
            job = 0
        else:
            job -= limit
            cycles += limit
        if job:
            queue.append((index, job))
        elif index == target:
            break
    return cycles
