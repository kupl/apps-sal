from math import gcd
from functools import reduce

def DPC_sequence(s):
    def lcm(a, b):
        return a*b // gcd(a, b)
    
    d, p, c = [], [], []
    for i in range(len(s)):
        if s[i] == "D": 
            d.append(i+1)
        elif s[i] == "P":
            p.append(i+1)
        else:
            c.append(i+1)
    
    if not d:
        return -1
    lcm_d = reduce(lambda i, j: lcm(i, j), d)
    for i in p:
        if gcd(lcm_d, i) != 1:
            return -1
    for i in c:
        if lcm_d % i == 0 or gcd(lcm_d, i) == 1:
            return -1
    return lcm_d

