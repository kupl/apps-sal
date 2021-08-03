def get_size(w, h, d):
    x = []
    x.append(2 * w * h + 2 * w * d + 2 * d * h)
    x.append(w * h * d)
    return x
