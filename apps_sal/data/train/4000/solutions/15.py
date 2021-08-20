import math


def strong_num(number):
    return 'STRONG!!!!' if number == sum([math.factorial(int(d)) for d in str(number)]) else 'Not Strong !!'
