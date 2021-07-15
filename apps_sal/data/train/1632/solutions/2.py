from math import log2


def countOnes(left, right): return countUpTo(right) - countUpTo(left-1)

def countUpTo(n):
    s = 0
    while n:
        p = n.bit_length()-1
        p2 = 1<<p
        s += p * (p2>>1) + n-p2+1
        n &= ~p2
    return s
