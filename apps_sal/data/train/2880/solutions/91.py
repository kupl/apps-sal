import math


def seven(m):
    num = m
    count = 0
    while num > 99:
        num = num // 10 - 2 * (num % 10)
        count += 1
    return (num, count)
