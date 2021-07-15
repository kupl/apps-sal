def get_size(w, h, d):
    listed = []
    area = 2 * (w * h) + 2 * (h * d) + 2 * (w * d)
    volume = w * h * d
    listed.append(area)
    listed.append(volume)
    return listed
