from math import factorial

def choose(n, x):
    return factorial(n) // (factorial(x) * factorial(n-x)) if x else 1

def checkchoose(m, n):
    for x in range(n+1):
        if choose(n, x) == m:
            return x
    return -1
