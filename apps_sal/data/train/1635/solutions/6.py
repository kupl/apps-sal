from math import factorial


def factoradic_representation(n):
    res = []
    i = 1
    while n > 0:
        res.append(n % i)
        n = n // i
        i += 1
    return res[::-1]


def middle_permutation(string):
    if len(string) < 2:
        return string
    s = sorted(string)
    res = []
    fr = factoradic_representation(factorial(len(s)) // 2 - 1)
    fr = [0] * (len(string) - len(fr)) + fr
    for idx in fr:
        res.append(s.pop(idx))
    return "".join(res)
