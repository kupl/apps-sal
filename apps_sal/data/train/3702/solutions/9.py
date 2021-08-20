import math
one = 'abdegopqADOPQR'


def olympic_ring(string):
    c = 0
    for x in string:
        if x == 'B':
            c = c + 2
        if x in one:
            c = c + 1
    c = math.floor(c / 2)
    if c > 3:
        return 'Gold!'
    if c == 3:
        return 'Silver!'
    if c == 2:
        return 'Bronze!'
    return 'Not even a medal!'
