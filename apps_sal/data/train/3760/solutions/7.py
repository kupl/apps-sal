def roundRobin(jobs, sl, index):
    start_sum = sum(jobs)
    cur_idx = 0
    while jobs[index] > 0:
        jobs[cur_idx] = jobs[cur_idx] - min(jobs[cur_idx], sl)
        cur_idx = (cur_idx + 1) % len(jobs)
    return start_sum - sum(jobs)
