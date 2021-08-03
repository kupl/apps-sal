def count_number(n, x):
    return len([j for j in range(1, n + 1) if x % j == 0 and x / j <= n])
