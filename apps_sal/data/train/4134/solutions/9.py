from math import ceil


def cooking_time(n, m, s, p):
    return '{0} minutes {1} seconds'.format(*divmod(ceil((m * 60 + s) * int(n[:-1]) / int(p[:-1])), 60))
