from math import factorial

def total_inc_dec(x):
    return comb(x + 10, 10) + comb(x + 9, 9) - 1 - (10 * x)  
    
def comb(n, k):
    f = factorial
    return f(n) // f(k) // f(n-k)
