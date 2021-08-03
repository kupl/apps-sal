def sum_mul(n, m):
    print(n, m)
    if n <= 0 or m <= 0:
        return "INVALID"
    return sum(i for i in range(m) if i % n == 0)
