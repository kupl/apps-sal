def queue_time(customers, n):
    tills = [0] * n
    for i in customers:
        indexMin = tills.index(min(tills))
        tills[indexMin] += i
    return max(tills)
