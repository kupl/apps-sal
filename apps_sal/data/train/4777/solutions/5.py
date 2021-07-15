def mystery_range(s,n):
    l=len(s)
    d=l-2*n
    if d==0 and n<90:
        ls=[10*int(s[i])+int(s[i+1]) for i in range(0,l,2)]
        return [min(ls), max(ls)]
    if abs(d)<n-90:
        return [10-(n-90-d)/2, 99+(n-90+d)/2]
    if d<0:
        return [10+d, 9+d+n]
    if d>0:
        return [100+d-n,99+d]
