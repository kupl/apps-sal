from itertools import count

def S_F(n):
    return 2**(-2 + n)*(3 + 3**n)

def find_mult10_SF(n):
    i = 0
    while n:
        i += 1
        sf = S_F(i)
        n -= (sf % 10 == 0)
    return sf
