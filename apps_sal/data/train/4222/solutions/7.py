def get_size(w,h,d):
    sa = 2*(w*d + h*d + w*h)
    vol = w*h*d
    return [sa,vol]
