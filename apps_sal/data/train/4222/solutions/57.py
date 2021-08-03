def get_size(w, h, d):
    S = (2 * w * d) + (2 * w * h) + (2 * d * h)
    V = w * h * d
    return [S, V]
