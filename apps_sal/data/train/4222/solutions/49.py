def get_size(w, h, d):
    area = w * d * 2 + d * h * 2 + w * h * 2
    volume = int(w) * int(d) * int(h)
    return [area, volume]
