def isqrt(num):
    '''Compute int(sqrt(n)) for n integer > 0
    O(log4(n)) and no floating point operation, no division'''
    res, bit = 0, 1
    while bit <= num:
        bit <<= 2
    bit >>= 2

    while bit:
        if num >= res + bit:
            num -= res + bit
            res += bit << 1
        res >>= 1
        bit >>= 2
    return res

def sqrt(n):
    # return n ** .5                                 ## Nope
    # return __import__('math').sqrt(n)              ## Not enough precision...
    # return __import__('decimal').Decimal(n).sqrt() ## That one works great!
    return isqrt(n) ## The very best, you don't need those nasty floating point numbers

def s_num(n):
    return sqrt(n) ** 2 == n

def g_p_num(n):
    return s_num(24 * n + 1)

def p_num(n):
    return g_p_num(n) and sqrt(24 * n + 1) % 6 == 5

def s_p_num(n):
    return s_num(n) and p_num(n) 
