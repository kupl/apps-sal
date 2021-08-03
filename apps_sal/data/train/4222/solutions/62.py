def get_size(w, h, d):
    area = 2 * (w * h + w * d + h * d)
    volumen = w * h * d
    result = [area, volumen]
    return result
