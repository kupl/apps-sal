from math import factorial


def strong_num(number):
    return 'STRONG!!!!' if sum(factorial(int(digit)) for digit in f'{number}') == number else 'Not Strong !!'
