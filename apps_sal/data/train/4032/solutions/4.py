from math import factorial

def binominal(n, k):
    if k < 0 or n < k:
        return None
    product = 1
    for i in range(k):
        product *= n-i
        product //= i+1
    return product

def catalan(n):
    return binominal(2*n, n) // (n+1)

def solve(n):
    return catalan(n)
