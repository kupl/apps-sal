def roundRobin(jobs, slice, index):
    total_cc = 0
    while True:
        for idx in range(len(jobs)):
            cc = min(jobs[idx], slice)
            jobs[idx] -= cc
            total_cc += cc
            if idx == index and jobs[idx] == 0:
                return total_cc
