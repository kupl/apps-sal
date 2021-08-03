def get_size(w, h, d):
    volume = w * h * d
    total_surface_area = 2 * (w * h + h * d + w * d)
    return [total_surface_area, volume]
