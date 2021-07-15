def numberOfSteps(steps, m):
    if steps < m:
        return -1
    q, r = divmod(steps, 2)
    q, r = divmod(q + r, m)
    return (q + (r > 0)) * m
