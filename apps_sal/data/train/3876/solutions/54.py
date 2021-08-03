def find(n):
    return sum(x for x in range(3, n + 1) if not x % 3 or not x % 5)
