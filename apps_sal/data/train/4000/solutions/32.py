from math import factorial


def strong_num(number):
    x = sum((factorial(int(d)) for d in str(number)))
    return 'STRONG!!!!' if x == number else 'Not Strong !!'
