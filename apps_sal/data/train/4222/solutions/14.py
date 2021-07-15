def get_size(w,h,d):
    area = (2 *(w*h)) + (2 *(w*d)) + (2 *(d*h))
    volume = w * h * d
    return [area, volume]
