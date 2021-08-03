def get_size(w, h, d):
    w = int(w)
    h = int(h)
    d = int(d)
    surface_area = 2 * w * h + 2 * h * d + 2 * d * w
    volume = (w * h * d)
    return [surface_area, volume]
