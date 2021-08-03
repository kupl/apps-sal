def nth_fib(n):
    return nth_fib(n - 2) + nth_fib(n - 1) if n > 2 else n - 1
