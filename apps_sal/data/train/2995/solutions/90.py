def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    a = 0
    b = []
    while a + n < m:
        a += n
        b.append(a)
    return sum(b)
