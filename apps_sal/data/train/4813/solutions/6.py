def get_num(n):
    holes = {'0': 1, '6': 1, '8': 2, '9': 1}
    return sum((holes[d] if d in holes else 0 for d in str(n)))
