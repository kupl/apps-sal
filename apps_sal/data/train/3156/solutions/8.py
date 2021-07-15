from math import floor, ceil, sqrt

def allEven(n):
    digs = list(str(n))
    odd_digs = ["1","3","5","7","9"]
    for dS in odd_digs:
        if dS in digs: return False
    return True

def even_digit_squares(a, b):
    lim1, lim2  = int(floor(sqrt(a))) - 1, int(ceil(sqrt(b)) + 1)
    res = []
    for i in range(lim1, lim2):
        ii = i**2
        if a<= ii <= b and allEven(ii):res.append(ii)
    return res
