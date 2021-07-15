def queue_time(customers, n):
    queues = [0] * n
    for i in customers:
        queues.sort()
        queues[0] += i
    return max(queues)
