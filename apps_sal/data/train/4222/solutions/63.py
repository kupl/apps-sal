def get_size(w,h,d):
    return [sum([w*h,h*d,d*w])*2,w*h*d]
