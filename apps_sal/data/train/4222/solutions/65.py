def get_size(w, h, d):
    s = 2 * (w * h + w * d + h * d)
    r = w * h * d
    return [s, r]
