memo = {}


def fibonacci(n):
    if n in [0, 1]:
        return n
    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]
