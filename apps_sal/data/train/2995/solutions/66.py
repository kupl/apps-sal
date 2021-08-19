def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    arr = [a * n for a in range(1, m) if a < m / n]
    return sum(arr)
