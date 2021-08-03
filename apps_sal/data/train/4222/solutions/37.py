def get_size(w, h, d):
    volume = w * h * d
    area = (w * h + h * d + w * d) * 2
    return [area, volume]
