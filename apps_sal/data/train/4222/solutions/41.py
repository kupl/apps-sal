def get_size(w, h, d):
    a = (2 * d * w) + (2 * d * h) + (2 * h * w)
    v = w * h * d
    return[a, v]
