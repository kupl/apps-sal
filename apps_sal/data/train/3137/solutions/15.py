from math import ceil as c, floor as f


def round_it(n):
    k, l = map(len, str(n).split('.'))
    return eval('[[c,f][k>l],round][k==l](n)')
