from math import log

def last_man_standing(n):
    return 1 + sum((((n >> i) | (i + 1)) % 2) << i for i in range(int(log(n, 2))))
