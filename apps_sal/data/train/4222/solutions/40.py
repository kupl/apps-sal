def get_size(w, h, d):
    volume = w * h * d
    area = 2 * (h * w) + 2 * (h * d) + 2 * (w * d)
    box = []
    box.append(area)
    box.append(volume)
    return box
