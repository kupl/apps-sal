def f(n):
    # your code here
    return [2**i if i != n + 1 else 2**i - 1for i in range(n+2)]
