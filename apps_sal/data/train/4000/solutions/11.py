import math


def strong_num(number):
    d = [int(d) for d in str(number)]
    b = sum([math.factorial(x) for x in d])
    if b == number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
