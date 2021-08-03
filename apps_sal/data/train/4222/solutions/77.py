def get_size(w, h, d):
    volume = w * h * d
    area = (w * 2 + h * 2) * d + w * h * 2
    array = [area, volume]
    return array
