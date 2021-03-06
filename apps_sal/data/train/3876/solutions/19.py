def find(n):
    (k1, k2, k3) = (n // 3, n // 5, n // 15)
    return (3 * k1 * (k1 + 1) >> 1) + (5 * k2 * (k2 + 1) >> 1) - (15 * k3 * (k3 + 1) >> 1)
