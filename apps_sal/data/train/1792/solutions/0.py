def three_by_n(n):
    A = [1, 2] + [0] * (n - 1)
    B = [0, 1] + [0] * (n - 1)
    C = [1, 0] + [0] * (n - 1)
    D = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        A[i] = A[i - 2] + 2 * B[i - 1] + 2 * C[i - 1] + 2 * D[i] + 2 * D[i - 2]
        B[i] = A[i - 1] + B[i - 2] + C[i - 2] + D[i - 1]
        C[i] = C[i - 2] + 2 * D[i - 1]
        D[i] = C[i - 1] + D[i - 2]
    return A[n] % 12345787
