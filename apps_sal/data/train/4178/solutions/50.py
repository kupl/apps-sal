def min_sum(A):
    A = sorted(A)
    l = len(A)
    return sum((a * b for (a, b) in zip(A[:l // 2], A[l // 2:][::-1])))
