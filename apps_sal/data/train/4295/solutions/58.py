def balanced_num(x):
    b=str(x)
    a=x
    q=0
    w=0
    if len(b)%2!=0:
        for i in b[0:int((len(b)/2)-0.5)]:
            q+=int(i)
        for i in b[int((len(b)/2)+0.5):]:
            w+=int(i)
    else:
        for i in b[0:int((len(b)/2)-1)]:
            q+=int(i)
        for i in b[int((len(b)/2)+1):]:
            w+=int(i)
    if q==w:
        return 'Balanced'
    else:
        return 'Not Balanced'
