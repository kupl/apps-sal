from fractions import gcd
def lcm(*args):
    m = 1 
    for i in args:
        if i == 0:
            return 0
        m = m*i/gcd(m,i)
    return m
        

