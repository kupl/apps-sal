def min_value(digits):
    new_digs = sorted(set(digits))
    a = ''
    for x in new_digs:
        a += str(x)
    return int(a)
