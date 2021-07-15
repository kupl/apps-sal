def solution(number):
    number -= 1
    f = lambda d, n: (d + n * d) * n / 2
    return f(3, number // 3) + f(5, number // 5) - f(15, number // 15)
