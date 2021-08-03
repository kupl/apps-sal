import math


def strong_num(number):
    result = 0
    number1 = number
    number2 = []
    while number1 > 0.99:
        number2.append(number1 % 10)
        number1 = int(number1 / 10)
    for i in number2:
        if i == 0:
            result += 1
        else:
            result += (math.factorial(i))
    if result == number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
