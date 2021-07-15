def pf(n):
    p,x = [],2
    while x*x <= n:
        while not n%x:
            n //= x
            p.append(x)
        x += 1
    if n>1:
        p.append(n)
    return p

def big_primefac_div(n):
    if isinstance(n,float) and not n.is_integer(): return "The number has a decimal part. No Results"
    n = abs(n)
    p = pf(n)
    return [p[-1],n//p[0] if n%2 else n//2] if p[-1]!=n else []
