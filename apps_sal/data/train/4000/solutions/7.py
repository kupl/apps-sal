import math


def strong_num(number):
    return ('Not Strong !!', 'STRONG!!!!')[sum(math.factorial(int(n)) for n in str(number)) == number]
