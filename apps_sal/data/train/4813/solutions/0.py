def get_num(n):
    return sum(({'0': 1, '6': 1, '9': 1, '8': 2}.get(d, 0) for d in str(n)))
