from math import factorial

def strong_num(number):
    sf = sum(factorial(int(c)) for c in str(number))
    return 'STRONG!!!!' if sf == number else 'Not Strong !!'
