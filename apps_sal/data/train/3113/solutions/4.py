def distribute(m, n):
    if m <= 0:
        return [0] * n
    elif n <= 0:
        return []
    else:
        a, b = divmod(m, n)
        return [a] * n if b == 0 else [a + 1] * b + [a] * (n - b)
