def sum_str(a, b):
    if len(a) == 0 and len(b) == 0:
        return '0'
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    else:
        m = int(a) + int(b)
        return str(m)
