def sum_str(*args):
    return str(sum(map(int, filter(None, args))))
