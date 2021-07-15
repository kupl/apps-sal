def segment_cover(A, L):
    A = sorted(A)
    nb_segments = 0
    while A:
        nb_segments += 1
        first_elt = A.pop(0)
        while A and A[0] <= first_elt + L:
            A.pop(0) 
    return nb_segments
    

