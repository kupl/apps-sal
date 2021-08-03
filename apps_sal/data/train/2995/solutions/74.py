def sum_mul(n, m):
    if n > 0 and m > 0:
        a = (m - 1) // n
        b = a * (a + 1)
        c = n - 2
        return b + c * (b / 2)
    return "INVALID"
