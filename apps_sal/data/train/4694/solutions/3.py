from math import factorial


def sum_fib(n):
    fibo_num = 1
    fibo_num_prev = 0
    sum_factorial = 0
    for num in range(0, n):
        sum_factorial = sum_factorial + factorial(fibo_num_prev)
        (fibo_num_prev, fibo_num) = (fibo_num, fibo_num + fibo_num_prev)
    return sum_factorial
