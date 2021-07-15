def get_size(w,h,d):
    v = w * h * d
    a = 2*(w*h+w*d+h*d)
    x = [a, v]
    return x
