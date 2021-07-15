def highest_value(*args):
    return max(args, key=lambda s:sum(map(ord, s)))
