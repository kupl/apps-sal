def get_size(w, h, d):
    A, S = 0, 0
    A = (2 * (h * w) + 2 * (h * d) + 2 * (w * d))
    S = (w * h * d)
    return list([A, S])
