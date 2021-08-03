import math


def balanced_num(number):
    num = [int(x) for x in str(number)]
    a = 0
    b = 0
    if len(num) % 2 == 1:
        a = sum(num[:len(num) // 2])
        b = sum(num[len(num) // 2 + 1:])
    else:
        a = sum(num[:len(num) // 2 - 1])
        b = sum(num[len(num) // 2 + 1:])
    if a == b:
        return "Balanced"
    else:
        return "Not Balanced"
