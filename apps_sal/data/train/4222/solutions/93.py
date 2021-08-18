def get_size(w, h, d):
    area = 2 * (w * h + h * d + w * d)
    vol = w * h * d
    a = [area, vol]
    return a
