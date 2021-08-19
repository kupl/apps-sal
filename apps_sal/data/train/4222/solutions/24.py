def get_size(w, h, d):
    surface = 2 * (w * h + h * d + d * w)
    area = w * h * d
    return [surface, area]
