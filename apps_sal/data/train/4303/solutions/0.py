from math import factorial as fact

def sum_arrangements(n):
    s = str(n)
    perms   = fact(len(s)-1)
    coefAll = int('1'*len(s))
    return coefAll*perms*sum(map(int,s))
