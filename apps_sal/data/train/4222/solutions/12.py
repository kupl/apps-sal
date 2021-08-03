def get_size(w, h, d):
    area = 2 * (w * h + h * d + d * w)
    volume = w * h * d
    return [area, volume]
