def solution(number):
    x = number - 1
    def f(n): return n * (n + 1) // 2
    return 3 * f(x // 3) + 5 * f(x // 5) - 15 * f(x // 15)
