from math import factorial

def choose(n, k):
    return factorial(n) / ( factorial(k) * factorial(n-k) ) if k <=n else 0
