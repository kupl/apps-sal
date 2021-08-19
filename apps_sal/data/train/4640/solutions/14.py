def int_diff(A, n):
    return sum((n == abs(b - a) for (i, a) in enumerate(A) for b in A[i + 1:]))
