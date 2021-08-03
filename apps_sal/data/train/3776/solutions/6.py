def segment_cover(A, l):
    A = set(A)
    m = min(A)
    c = 0
    while A:
        A = {a for a in A if a > m + l}
        c += 1
        if A:
            m = min(A)
        else:
            return c
