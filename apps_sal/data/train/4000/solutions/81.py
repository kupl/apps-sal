from math import factorial as fact


def strong_num(n):
    return 'STRONG!!!!' if sum((fact(int(c)) for c in str(n))) == n else 'Not Strong !!'
