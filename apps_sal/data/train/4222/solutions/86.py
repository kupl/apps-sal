def get_size(w,h,d):
    area = int(2*(h * w) + 2*(h * d) + 2*(d * w))
    volume = int(w) * int(h) * int(d)
    return [area, volume]
