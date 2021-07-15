import math
def sum_fib(n):
    fib_arr = []
    a, b = 0, 1
    for i in range(n):
        fib_arr.append(math.factorial(a))
        a, b = b, a + b
    return sum(fib_arr)
