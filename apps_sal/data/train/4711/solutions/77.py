import math


def zeros(n):
    return sum((int(n / math.pow(5, i)) for i in range(1, 15) if int(n / math.pow(5, i)) != 0))
