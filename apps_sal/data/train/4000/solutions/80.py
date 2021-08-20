import math


def strong_num(number):
    n = 0
    for i in str(number):
        n = n + math.factorial(int(i))
    if n == number:
        return 'STRONG!!!!'
    else:
        return 'Not Strong !!'
