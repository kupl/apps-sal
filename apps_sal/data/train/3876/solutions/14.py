def find(n):
    return sum((x for x in range(n + 1) if not (x % 3 and x % 5)))
