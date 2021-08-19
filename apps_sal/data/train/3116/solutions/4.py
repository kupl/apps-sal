def cal_n_bug(h, l, p):
    # s+d+b=h / 8s+6d+6b=l / 0s+2d+b=p
    d = l / 2 - 4 * h + p
    b = p - 2 * d
    s = h - d - b
    return [-1, -1, -1] if s < 0 or b < 0 or d < 0 else [s, b, d]
