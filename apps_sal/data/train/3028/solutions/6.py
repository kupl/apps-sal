from math import factorial as f

def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    return f(n)
