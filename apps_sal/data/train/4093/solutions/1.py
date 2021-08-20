def find_a(A, n):
    if 0 <= n < 4:
        return A[n]
    if n < 0:
        (A, n) = (A[::-1], abs(n) + 3)
    B = [0] * 4
    B[1] = 3 * A[1] - A[0] - A[2]
    B[2] = 3 * A[2] - A[1] - A[3]
    B[3] = 3 * B[2] - B[1] - A[2]
    ind = 4
    while ind <= n:
        a = 3 * A[-1] - A[-2] - B[-1]
        b = 3 * B[-1] - B[-2] - A[-1]
        A.append(a)
        B.append(b)
        ind += 1
    return A[-1]
