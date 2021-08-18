def countWays(n):
    A = [0] * (n + 1)
    B = [0] * (n + 1)
    A[0] = 1
    A[1] = 2
    B[0] = 0
    B[1] = 1
    for i in range(2, n + 1):
        if (i % 2):
            B[i] = (A[i - 1] + B[i - 2]) % 12345787
            A[i] = (A[i - 2] + 2 * B[i] + 2 * B[i - 1]) % 12345787
        else:
            A[i] = (A[i - 2] + 2 * B[i - 1]) % 12345787
            B[i] = (A[i - 1] + A[i - 2] + B[i - 1] + B[i - 2]) % 12345787
    return A[n]


def three_by_n(n):
    return countWays(n)
