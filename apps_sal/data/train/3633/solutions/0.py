def shuffle_it(A, *T):
    for (x, y) in T:
        (A[x], A[y]) = (A[y], A[x])
    return A
