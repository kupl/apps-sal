def find(n):
    return sum(set([x for x in range(0, n + 1, 3)] + [x for x in range(0, n + 1, 5)]))
