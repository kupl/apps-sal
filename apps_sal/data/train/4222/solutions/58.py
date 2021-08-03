def get_size(w, h, d):
    # your code here
    area = 0
    volume = 0

    area = 2 * w * h + 2 * h * d + 2 * w * d
    volume = w * h * d

    return [area, volume]
