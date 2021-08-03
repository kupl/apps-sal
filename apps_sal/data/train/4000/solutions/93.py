import math


def strong_num(number):
    total = 0
    for i in str(number):
        total += math.factorial(int(i))
    return "STRONG!!!!" if total == number else "Not Strong !!"
