from math import factorial

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]


def sum_fib(n):
    return sum(factorial(x) for x in fib[:n])
