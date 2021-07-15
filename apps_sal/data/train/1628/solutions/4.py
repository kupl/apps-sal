from fractions import Fraction

# Euler's totient function
# Prime factors search can be easily optimize but it's already really fast anyway
def proper_fractions(n):
    res = Fraction(n)
    for i in range(2, int(n**0.5)+1):
        if n%i: continue
        while not n%i: n //= i
        res *= Fraction(i-1, i)
        if n == 1: break
    else: res *= Fraction(n-1, n)
    return res
