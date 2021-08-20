def val(x):
    return x * (x + 1) >> 1


def solution(number):
    res1 = 3 * val((number - 1) // 3)
    res2 = 5 * val((number - 1) // 5)
    res3 = 15 * val((number - 1) // 15)
    return res1 + res2 - res3
