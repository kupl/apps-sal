def chess_bishop_dream(b, p, d, k):
    yq, yr = divmod(p[0] + k * d[0], b[0])
    xq, xr = divmod(p[1] + k * d[1], b[1])
    if yq < 0:
        yq = -yq
        yr = b[0] - yr - 1
    if xq < 0:
        xq = -xq
        xr = b[1] - xr - 1
    return [(b[0] - yr - 1 if yq % 2 == (d[0] > 0) else yr), (b[1] - xr - 1 if xq % 2 == (d[1] > 0) else xr)]
