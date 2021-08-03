def get_size(w, h, d):
    area = 2 * (h * w) + 2 * (h * d) + 2 * (w * d)
    return [area, w * d * h]
