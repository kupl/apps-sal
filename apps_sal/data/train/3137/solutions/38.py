import math


def round_it(n):
    lst = list(str(n))
    i = lst.index('.')
    print(lst)
    if len(lst[0:i]) > len(lst[i:-1]):
        return math.floor(n)
    elif len(lst[0:i]) < len(lst[i:-1]):
        return math.ceil(n)
    else:
        return round(n)
