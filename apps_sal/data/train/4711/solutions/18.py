def zeros(n):
    base, total = 5, 0
    while n>base:
        total += n // base
        base *= 5
    return total
