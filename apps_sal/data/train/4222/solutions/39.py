def get_size(w, h, d):
    total_area = 2 * (h * d) + 2 * (w * h) + 2 * (d * w)
    volume = w * d * h
    x = [total_area, volume]
    return x
