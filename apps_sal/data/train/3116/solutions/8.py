def cal_n_bug(h, l, w):
    if h < 0 or l < 0 or w < 0 or l % 2 or l < 6 * h or l > 8 * h:
        return [-1, -1, -1]
    d, b = w // 2, w % 2
    s = h - d - b
    return [h - d - b, b, d] if s * 8 + d * 6 + b * 6 == l else [-1, -1, -1]
