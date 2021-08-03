from math import factorial


def strong_num(number):
    sum = 0
    for el in str(number):
        sum += factorial(int(el))
    if sum == number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
