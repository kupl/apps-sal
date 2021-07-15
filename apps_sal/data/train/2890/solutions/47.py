def multiples(m, n):
    count = [x * n for x in range(1, m + 1) if x > 0]
    return count
