from math import factorial


def strong_num(number):
    s = 0
    for x in str(number):
        s += factorial(int(x))
    return 'STRONG!!!!' if s == number else 'Not Strong !!'
