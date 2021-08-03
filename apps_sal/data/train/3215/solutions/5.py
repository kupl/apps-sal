def reduce_pyramid(Q):
    R, U = 0, 1
    for F, V in enumerate(Q):
        R, U = R + V * U, U * (len(Q) + ~F) // -~F
    return R
