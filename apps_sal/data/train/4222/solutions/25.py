def get_size(w,h,d):
    #your code here
    s = []
    area = 2 * ((w * h) + (h * d) + (w * d))
    sa = w * d * h
    s.append(area)
    s.append(sa)
    return (s)
