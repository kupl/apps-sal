def SJF(jobs, index):
    return sum(n for i, n in enumerate(jobs) if n < jobs[index] or (n == jobs[index] and i <= index))

    #jobs = jobs.copy()
    #cycles = 0
    # for n in sorted(jobs):
    #    cycles += n
    #    i = jobs.index(n)
    #    jobs[i] = 0
    #    if i == index:
    #        break
    # return cycles
