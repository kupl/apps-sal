def summ(number, d):
    n = (number - 1) // d
    return n * (n + 1) * d // 2


def solution(number):
    return summ(number, 3) + summ(number, 5) - summ(number, 15)
