from math import ceil


def digits_average(input):
    if input < 10:
        return input
    else:
        l = [int(i) for i in list(str(input))]
        r = [ceil(sum(i) / 2.0) for i in list(zip(l, l[1:]))]
        return r[0] if len(r) == 1 else digits_average(int(''.join([str(i) for i in r])))
