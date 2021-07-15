def count_black_cells(h, w):
    if h==w:
        return 3*h-2
    r=0
    x1=0
    for i in range(h):
        x2=w*(i+1)/h
        r+=(int(x2)+1)-int(x1)
        if int(x1)==x1 and x1!=0:
            r+=1
        elif i==h-1:
            r-=1
        x1=x2
    return r
