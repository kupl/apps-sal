def triple_shiftian(T, n):
    for i in range(3, n + 1):
        T.append(4 * T[i - 1] - 5 * T[i - 2] + 3 * T[i - 3])
    return T[n]
