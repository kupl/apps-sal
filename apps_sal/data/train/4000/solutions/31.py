from math import factorial


def strong_num(n):
    return 'STRONG!!!!' if sum((factorial(int(d)) for d in str(n))) == n else 'Not Strong !!'
