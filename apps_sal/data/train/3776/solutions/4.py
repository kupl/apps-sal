def segment_cover(A, L):
    end = None
    count = 0
    for a in sorted(A):
        if end and a <= end:
            continue
        else:
            end = a + L
            count += 1
    return count
