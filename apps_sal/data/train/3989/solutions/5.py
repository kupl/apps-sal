def f(a, x):
    n = x // a
    return n * a * (n + 1) // 2

def solution(n):
    return f(3, n-1) + f(5, n-1) - f(15, n-1)
