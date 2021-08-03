def two_by_n(n, k):
    if n == 1:
        return k
    F = [0 for k in range(n + 1)]
    G = [0 for k in range(n + 1)]
    F[1] = 1
    F[2] = k - 1
    G[2] = 1
    for i in range(3, n + 1):
        F[i] = (k - 1) * F[i - 1] + (k - 1) * (k - 2) * G[i - 1]
        G[i] = (k - 2) * F[i - 2] + (k * k - 3 * k + 3) * G[i - 2]

    return (k * F[n] + k * (k - 1) * G[n]) % 12345787
