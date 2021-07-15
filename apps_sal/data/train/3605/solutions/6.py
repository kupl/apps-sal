from math import factorial
def diagonal(n,p):
    s=factorial(n+1)//(factorial(p+1)*factorial(n-p))
    return int(s)
