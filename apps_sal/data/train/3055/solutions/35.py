def sum_str(*args):
    return str(sum(int(x) for x in args if x != ''))
