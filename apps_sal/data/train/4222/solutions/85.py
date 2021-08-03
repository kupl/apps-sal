def get_size(w, h, d):
    total_area = 2 * (w * h + h * d + w * d)
    volume = w * h * d
    return [total_area, volume]
