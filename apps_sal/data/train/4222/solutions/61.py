def get_size(w, h, d):
    surface_area = []
    surface_area.append(2 * ((d * w) + (d * h) + (w * h)))
    surface_area.append((h * d) * w)
    return surface_area
