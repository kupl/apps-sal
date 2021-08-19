import math


def strong_num(number):
    n = list(map(int, str(number)))
    lst = [math.factorial(i) for i in n]
    return 'STRONG!!!!' if sum(lst) == number else 'Not Strong !!'
