def min_sum(A):
    A = sorted(A)
    l = len(A)
    return sum(e1*e2 for e1, e2 in zip(A[:l//2], A[l//2:][::-1]))
