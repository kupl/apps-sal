from math import factorial


def strong_num(n):
    return ['Not Strong !!', 'STRONG!!!!'][n == sum((factorial(int(d)) for d in str(n)))]
