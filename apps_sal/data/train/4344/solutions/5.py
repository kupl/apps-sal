from math import factorial

def rectangles(n, m):
    return 0 if n <= 1 or m <= 1 else round(factorial(n)/factorial(n-2)/2 * factorial(m)/factorial(m-2)/2)

