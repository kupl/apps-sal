from math import factorial


def strong_num(number):
    return ("Not Strong !!", "STRONG!!!!")[sum(factorial(int(i)) for i in str(number)) == number]
