def queue_time(cu, n):
    q = [0] * n
    for i in cu:
        s = q.index(min(q))
        q[s] += i
    return max(q)
