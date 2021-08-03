def get_size(w, h, d):
    x = w * h * d
    y = (w * h + h * d + d * w) * 2
    return [y, x]
