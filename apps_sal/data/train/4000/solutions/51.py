import math


def strong_num(number):
    if sum(math.factorial(int(n)) for n in str(number)) == number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
