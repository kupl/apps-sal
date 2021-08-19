def solution(number):
    n = number - 1
    (a, b, c) = (n // 3, n // 5, n // 15)
    return [a - c, b - c, c]
