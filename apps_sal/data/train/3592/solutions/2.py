def lcm(a, b):
    from fractions import gcd
    return a * b // gcd(a, b)

def greatest(x, y, n):
    m = lcm(x, y)
    return (n//m)*m if m<n else 0
    
def smallest(x, y, n):
    m = lcm(x, y)
    return ((n+m)//m)*m
