def count_number(n, x):
    k = [1, x // n][x > n]
    return sum(1 for i in range(k, n + 1) if x/i == x//i and x/i in range(1, n + 1))
