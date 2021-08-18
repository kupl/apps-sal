import re


def zeroes(base, number):
    i = 2
    factors = []
    while i * i <= base:
        if base % i:
            i += 1
        else:
            base //= i
            factors.append(i)
    if base > 1:
        factors.append(base)

    count = 99999999999999999999
    for i in set(factors):
        sum = number // i
        temp = sum
        while temp >= i:
            temp //= i
            sum += temp
        sum //= factors.count(i)
        if sum < count:
            count = sum

    return count
