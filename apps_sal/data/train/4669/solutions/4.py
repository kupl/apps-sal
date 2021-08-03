def beggars(values, n):
    if n < 1:
        return []
    k = [0] * n
    for i in range(len(values)):
        k[i % n] += values[i]
    return k
