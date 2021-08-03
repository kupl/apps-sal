def sum_str(*a):
    return str(sum(map(lambda s: int(s) if s else 0, a)))
