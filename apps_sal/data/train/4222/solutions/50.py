def get_size(w,h,d):
    area = 2*(w*h)+2*(h*d)+2*(d*w)
    volume = w*h*d
    arr = [area,volume]
    return arr
