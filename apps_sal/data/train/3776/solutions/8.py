def segment_cover(A, L):
    c = 0
    while A:
        c+=1
        seg = min(A, default=0)
        A = list([item for item in A if item > seg+L])
    return c

