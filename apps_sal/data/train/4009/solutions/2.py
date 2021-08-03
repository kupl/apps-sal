import math


def digits_average(n):
    a = [int(i) for i in list(str(n))]
    e = [a[i:i + 2] for i in range(len(a) - 1)]
    return n if len(str(n)) == 1 else digits_average(int(''.join([str(math.ceil(sum(i) / 2)) for i in e])))
