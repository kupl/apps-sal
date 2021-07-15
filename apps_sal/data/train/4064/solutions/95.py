def count_by(n, x):
    return [i for i in range(n, (x + 1) * n) if i % n == 0]
