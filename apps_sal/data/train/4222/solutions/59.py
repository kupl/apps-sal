def get_size(w, h, l):
    a = 2 * l * w + 2 * l * h + 2 * w * h
    v = w * h * l
    return [a, v]
