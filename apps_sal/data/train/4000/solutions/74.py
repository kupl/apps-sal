import math


def strong_num(number):
    nums = [int(char) for char in str(number)]
    strong = 0
    for i in nums:
        strong += math.factorial(i)
    if strong == number:
        return 'STRONG!!!!'
    else:
        return 'Not Strong !!'
