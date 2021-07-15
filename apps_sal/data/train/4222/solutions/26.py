def get_size(w,h,d):
    volumn = w * h * d
    area = 2 * (w * h + h * d + d * w)
    return [area, volumn]
