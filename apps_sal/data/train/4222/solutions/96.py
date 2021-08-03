def get_size(w, h, d):
    total_area = 2 * (h * w) + 2 * (h * d) + 2 * (w * d)
    volume = w * h * d
    return [total_area, volume]
