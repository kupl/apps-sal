def triple_shiftian(base, n):
    num = [0] * (n + 1) if n > 3 else [0, 0, 0]
    (num[0], num[1], num[2]) = base
    i = 3
    while i <= n:
        num[i] = 4 * num[i - 1] - 5 * num[i - 2] + 3 * num[i - 3]
        i += 1
    return num[n]
