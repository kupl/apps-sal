from math import *


def pow_root_pandigit(val, n, k):
    """
    Create a function to give k smaller couples of the root - pandigital numbers with the power n
    and bigger than val.
    """
    l = []
    if val < 0:
        val = 0
    if val > 987654321:
        return l
    r = 1.0 / n
    for i in range(int(ceil((val + 1) ** r)), int(987654322 ** r)):
        string = str(i ** n)
        if len(set(string)) == len(string) and '0' not in string and ('0' not in str(i)) and (len(set(str(i))) == len(str(i))):
            l.append([i, int(string)])
        if len(l) == k:
            break
    if len(l) == 1:
        l = l[0]
    return l
