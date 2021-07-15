def get_size(w,h,d):
    r=[]
    a=2*w*h+2*h*d+2*w*d
    r.append(a)
    v=w*h*d
    r.append(v)
    return r
