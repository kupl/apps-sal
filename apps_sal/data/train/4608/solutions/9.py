def finance(n):
    return sum([sum(range(2 * a, 2 * n + 1 - 2 * a)) for a in range(n)])
