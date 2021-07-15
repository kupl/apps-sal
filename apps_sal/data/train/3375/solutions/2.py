def going(n):
    a = 1.
    for i in range(2, n+1):
        a/=i
        a+=1
    return float(str(a)[:8])
