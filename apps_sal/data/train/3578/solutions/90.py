def paperwork(n, m):
    if m<0:
        return 0
    if n<0:
        return 0
    if m==0:
        return 0
    if n==0:
        return 0
    if n>0 and m>0:
        return n*m
