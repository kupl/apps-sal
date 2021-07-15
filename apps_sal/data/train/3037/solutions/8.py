from collections import Counter

def obtain_max_number(arr):
    c=dict(Counter(arr))
    s=set(c)
    r=0
    while s:
        m=min(s)
        v=c[m]
        s-={m}
        M=m*2
        if v//2:
            c[M]=c.get(M,0)+v//2
            s|={M}
        r=max(r,m)
    return r
