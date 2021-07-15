from math import factorial

def sum_fib(n):
    t, a, b = 0, 0, 1
    while n:
        t += factorial(a)
        a, b, n = b, a+b, n-1
    return t
