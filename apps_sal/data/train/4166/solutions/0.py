import math

def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n//i])
    divs.extend([n])
    return list(set(divs))

def solve(p):
    for d in sorted(divisors(p-1)):
        if pow(10, d, p) == 1:
            return "{}-sum".format(d)
            break
        elif pow(10, d, p) == p-1:
            return "{}-altsum".format(d)
            break

