import math


def matrixfy(st):
    if not st:
        return 'name must be at least one letter'
    side = math.ceil(math.sqrt(len(st)))
    quad = side * side
    st += '.' * (quad - len(st))
    return [list(st[i - side:i]) for i in range(side, quad + 1, side)]
