import math


def round_it(n):
    print(n)
    count_whole = len(str(round(n)))
    count = len(str(n))
    if (count - 1 - count_whole) == count_whole:
        return round(n)
    elif (count - 1 - count_whole) > count_whole:
        return math.ceil(n)
    else:
        return math.floor(n)
