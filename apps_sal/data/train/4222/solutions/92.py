def get_size(w, h, d):
    SA = 2 * w * h + 2 * w * d + 2 * h * d
    V = h * w * d
    return [SA, V]
