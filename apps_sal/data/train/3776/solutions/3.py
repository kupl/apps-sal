def segment_cover(A, L):
    A = sorted(A)
    segment_end = A[0] - 1
    segments = 0
    for point in A:
        if point > segment_end:
            segments += 1
            segment_end = point + L
    return segments

