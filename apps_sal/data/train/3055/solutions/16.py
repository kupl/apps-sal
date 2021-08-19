def sum_str(*args):
    return str(sum((int(c) for c in args if c.isdigit())))
