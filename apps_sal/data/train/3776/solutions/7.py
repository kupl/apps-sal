def segment_cover(a,l):
    s=0
    while a:
        L=min(a)+l
        a=[v for v in a if v>L]
        s+=1
    return s
