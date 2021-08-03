from operator import *


def calculate(n1, n2, o):
    result = eval(o[:3])(int(n1, 2), int(n2, 2))
    return (bin(result)[2:], bin(result)[0] + bin(result)[3:])[result < 0]
