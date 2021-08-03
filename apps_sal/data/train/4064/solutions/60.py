def count_by(x, n):
    a = [i for i in range(x, x * n + 1) if i % x == 0]
    return a[:n + 1]
