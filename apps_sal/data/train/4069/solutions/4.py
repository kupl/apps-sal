def nth_fib(n):
    if n <= 2:
        return n - 1
    return nth_fib(n - 1) + nth_fib(n - 2)
