def fac(n):
    r = 1
    for x in range(1,n+1):
        r*=x
    return r
        
def strong_num(n):
    return "STRONG!!!!" if sum([fac(int(x)) for x in str(n)])==n else "Not Strong !!"
