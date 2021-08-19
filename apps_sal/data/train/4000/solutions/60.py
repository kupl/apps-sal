from math import factorial


def strong_num(number):
    s = str(number)
    return 'STRONG!!!!' if sum((factorial(int(n)) for n in s)) == number else 'Not Strong !!'
