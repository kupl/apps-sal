import math


def round_it(n):
    if (len(str(n)) + 1) / 2 > str(n).find(".") + 1:
        return math.ceil(n)
    elif (len(str(n)) + 1) / 2 == str(n).find(".") + 1:
        return round(n)
    elif (len(str(n)) + 1) / 2 < str(n).find(".") + 1:
        return math.floor(n)
