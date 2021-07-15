import math

def isPowerOfTwo (n):
    return (math.ceil(math.log2(n)) == math.floor(math.log2(n)))

def toothpick(n):
    """Returns number of picks required for n rounds of the toothpick sequence"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif isPowerOfTwo (n):
        return int((2**(2*math.log2(n)+1)+1) / 3)
    k = int (math.log2(n))
    i = n - 2**k
    
    return toothpick (2**k) + 2*toothpick(i) + toothpick (i+1) - 1
