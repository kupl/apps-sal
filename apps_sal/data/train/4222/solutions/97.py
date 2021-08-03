def get_size(w, h, d):
    l = []
    l.append(2 * (w * h + h * d + d * w))
    l.append(w * h * d)
    return l
