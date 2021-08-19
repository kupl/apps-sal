def queue_time(customers, n):
    tills = [0 for i in range(n)]
    for time in customers:
        min_index = tills.index(min(tills))
        tills[min_index] += time
    return max(tills)
