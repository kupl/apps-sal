def add(*args):
    return round(sum(value / pos for pos, value in enumerate(args, 1)))
