def get_size(w, h, d):
    vol = w * h * d
    surface = 2 * w * h + 2 * w * d + 2 * h * d
    return [surface, vol]
