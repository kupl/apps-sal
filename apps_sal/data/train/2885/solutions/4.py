from math import floor
def champernowneDigit(n):
    print(n)
    if n == None or isinstance(n, bool) or not isinstance(n, int) or n < 1: return float('nan')
    t, c = 10, 1
    while t < n: 
        c += 1
        t += 9 * 10**(c-1) * c
    num = str(10**c - 1 - floor((t-n)/c))
    return int(num[c - 1 - (t-n)%c])
