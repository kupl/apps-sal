from math import factorial


def strong_num(number):
    return ['Not Strong !!', 'STRONG!!!!'][number == sum((factorial(int(c)) for c in str(number)))]
