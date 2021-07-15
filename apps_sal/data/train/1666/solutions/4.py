from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def solution(a):
    return len(a) * reduce(gcd, a)
