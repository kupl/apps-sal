from functools import reduce

def factors(n):   
    a = set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    return [[i for i in range(2, int(n**0.5) + 1) if i**2 in a],[i for i in range(2, int(n**0.5) + 1) if i**3 in a]]

