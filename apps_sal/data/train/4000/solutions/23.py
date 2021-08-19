import math


def strong_num(number):
    for i in str(number):
        number -= math.factorial(int(i))
    return 'STRONG!!!!' if number == 0 else 'Not Strong !!'
