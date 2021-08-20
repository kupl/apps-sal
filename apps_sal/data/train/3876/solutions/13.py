def find(n):
    return sum((e for e in range(n + 1) if not e % 3 or not e % 5))
