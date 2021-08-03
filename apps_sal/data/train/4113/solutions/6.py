def solution(number):
    number = number - 1
    c = int(number / 15)
    b = int(number / 5) - c
    a = int(number / 3) - c
    return [a, b, c]
