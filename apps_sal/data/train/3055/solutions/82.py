def sum_str(a, b):
    if not a and not b:
        return '0'
    elif not a and b:
        return b
    elif not b and a:
        return a

    return str(int(a) + int(b))
