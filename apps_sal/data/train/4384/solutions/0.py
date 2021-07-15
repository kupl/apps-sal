from fractions import gcd

def fraction(a,b):
    return (a+b)//gcd(a,b)
