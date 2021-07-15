def candles(m,n):
    total=0
    l=0
    while m:
        total+=m
        m,l=divmod(m+l,n)
    return total
