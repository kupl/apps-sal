def segment_cover(A, L):
    n = 1
    s = min(A)
    for i in sorted(A):
        if s + L < i:
            s = i
            n += 1
    return n
