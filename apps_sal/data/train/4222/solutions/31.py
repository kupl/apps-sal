def get_size(w, h, d):
    area = 2 * h * (w + d) + 2 * w * d
    volume = w * d * h
    return [area, volume]
