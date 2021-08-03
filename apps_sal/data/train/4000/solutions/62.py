from math import factorial as f


def strong_num(number):
    factors = [f(int(x)) for x in str(number)]
    return 'STRONG!!!!' if sum(factors) == number else 'Not Strong !!'
