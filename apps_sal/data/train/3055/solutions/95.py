def sum_str(*args):
    return str(sum([int(arg) if arg != '' else 0 for arg in args]))
