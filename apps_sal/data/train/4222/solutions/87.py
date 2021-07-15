def get_size(w,h,d):
    vol = w * h * d
    sur = 2*(w*h + w*d + h*d)
    return [sur, vol]
