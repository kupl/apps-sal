from math import factorial


def strong_num(number):
    return "STRONG!!!!" if sum(factorial(int(v))for v in str(number)) == number else "Not Strong !!"
