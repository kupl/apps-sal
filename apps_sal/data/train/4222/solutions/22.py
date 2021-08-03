def get_size(w, h, d):
    area = w * h * d
    surface_area = 2 * w * h + 2 * h * d + 2 * w * d
    return [surface_area, area]
