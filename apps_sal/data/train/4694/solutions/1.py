from math import factorial

def sum_fib(n):
    a, b, s = 0, 1, 0
    while n:
        s += factorial(a)
        a, b = b, a+b
        n -= 1
    return s
