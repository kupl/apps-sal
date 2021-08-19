import math


def zeros(n):
    """factorial = 1
    count = 0
    if n <= 0:
        return 0
    for i in range(1, n + 1):
        factorial = factorial * 1"""
    count = 0
    'if n <= 0:\n        return 0\n    else:\n        fact = math.factorial(int(n))\n        check = True\n        while check:\n            if fact % 10 == 0:\n                count += 1\n            elif fact % 10 != 0:\n                check = False'
    i = 5
    while n / i >= 1:
        count += int(n / i)
        i *= 5
    return int(count)
