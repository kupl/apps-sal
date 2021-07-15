def get_exponent(n, p):
    if p <=1 : return 
    return max([i for i in range(1,int(abs(n)**.5)) if n% (p ** i)==0],default=0)
