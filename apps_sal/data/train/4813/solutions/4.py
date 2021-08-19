holes = {'0': 1, '6': 1, '8': 2, '9': 1}


def get_num(n):
    return sum((holes.get(c, 0) for c in str(n)))
