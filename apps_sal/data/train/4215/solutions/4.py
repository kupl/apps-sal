def count_number(n, x):
    return sum(range(i, i * n + 1, i).count(x) for i in range(1, n+1))
