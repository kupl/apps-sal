from math import factorial


def strong_num(n):
    return 'STRONG!!!!' if n == sum((factorial(int(c)) for c in str(n))) else 'Not Strong !!'
