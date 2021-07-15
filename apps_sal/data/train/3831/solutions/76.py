def angle(n):
    s=180
    p=0
    if n==3:
        return s
    if n>3:
        for i in range (3,n+1):
            p=p+s
    return p
