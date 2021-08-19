def get_size(w, h, d):
    return [(w * d + w * h + h * d) * 2, w * d * h]
