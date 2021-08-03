def sum_str(*args):
    return str(sum(map(lambda x: int(x) if x != '' else 0, args)))
