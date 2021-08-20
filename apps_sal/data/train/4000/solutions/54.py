import math


def strong_num(number):
    sum = 0
    number = str(number)
    for i in number:
        sum += math.factorial(int(i))
    if sum == int(number):
        return 'STRONG!!!!'
    else:
        return 'Not Strong !!'
