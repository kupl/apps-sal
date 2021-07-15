def fusc(n):
    if n <2:
        return n
    if n%2:
        m = (n-1)//2
        return fusc(m) + fusc(m+1)
    return fusc(n/2)
    

