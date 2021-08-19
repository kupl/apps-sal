import math


def strong_num(number):
    fact = 0
    for i in str(number):
        fact += math.factorial(int(i))
    return 'STRONG!!!!' if number == fact else 'Not Strong !!'
