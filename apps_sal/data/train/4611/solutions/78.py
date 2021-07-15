def animals(h, l):
    co = l/2 -h
    ch = h -co
    return (0,0) if h==0 and l==0 else "No solutions" if h<1 or l<1 or co<0 or ch<0 or l%2 != 0 else (ch,co)

