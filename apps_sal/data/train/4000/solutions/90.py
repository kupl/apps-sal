from math import factorial


def strong_num(n):
    return 'STRONG!!!!' if n == sum((factorial(int(d)) for d in str(n))) else 'Not Strong !!'
