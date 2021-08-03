import math


def strong_num(number):
    check = 0
    for i in str(number):
        check += math.factorial(int(i))
    return "STRONG!!!!" if check == number else "Not Strong !!"
