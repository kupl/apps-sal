def segments(m, a):
    return [x for x in range(m + 1) if all((x not in range(A[0], A[1] + 1) for A in a))]
