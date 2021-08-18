def triple_shiftian(base, n):
    for i in range(n - 2):
        base.append(4 * base[i + 2] - 5 * base[i + 1] + 3 * base[i])
    return base[n]
