from collections import Counter

def solve(a,b):
    return sum((Counter(a)-Counter(b)).values()) if Counter(b) - Counter(a) == {} else 0 
