def chess_bishop_dream(b, p, d, k):
    (yq, yr) = divmod(p[0] + k * d[0], 2 * b[0])
    (xq, xr) = divmod(p[1] + k * d[1], 2 * b[1])
    return [min(yr, 2 * b[0] - yr - 1), min(xr, 2 * b[1] - xr - 1)]
