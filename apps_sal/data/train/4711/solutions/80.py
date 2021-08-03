import math


def zeros(n):
    '''factorial = 1
    count = 0
    if n <= 0:
        return 0
    for i in range(1, n + 1):
        factorial = factorial * 1'''
    count = 0
    '''if n <= 0:
        return 0
    else:
        fact = math.factorial(int(n))
        check = True
        while check:
            if fact % 10 == 0:
                count += 1
            elif fact % 10 != 0:
                check = False'''

    i = 5
    while (n / i >= 1):
        count += int(n / i)
        i *= 5

    return int(count)
