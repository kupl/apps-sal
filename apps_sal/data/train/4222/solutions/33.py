def get_size(w,h,d):
    #your code here
    l=[]
    a=2*(w*h)+2*(h*d)+2*(w*d)
    v=w*h*d
    l.append(a)
    l.append(v)
    return l
