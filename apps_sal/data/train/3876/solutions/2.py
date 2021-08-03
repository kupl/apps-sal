def find(n):
    return sum(range(0, n + 1, 3)) + sum(range(0, n + 1, 5)) - sum(range(0, n + 1, 15))
