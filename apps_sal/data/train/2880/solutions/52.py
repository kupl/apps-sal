def seven(m):
    s = str(m)
    c = 0
    while len(s) > 2:
        x,y = int(s[:-1]),int(s[-1])
        z = x-2*y
        s = str(z)
        c = c+1
    return (int(s),c)
