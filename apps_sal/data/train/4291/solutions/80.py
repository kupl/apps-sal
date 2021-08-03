from math import *


def century(year):
    x = 0
    if year % 100 == 0:
        x = floor(int((year + 1) / 100))
    else:
        x = floor(int(year / 100 + 1))
    return x


print(century(1249))
