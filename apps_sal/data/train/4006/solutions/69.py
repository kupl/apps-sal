def basic_op(operator, value1, value2):
    p = '-'
    s = '+'
    r = '*'
    e = '/'
    if p in operator:
        return value1 - value2
    elif s in operator:
        return value1 + value2
    elif r in operator:
        return value1 * value2
    elif e in operator:
        return value1 / value2
