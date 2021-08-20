def sum_str(a, b):
    if a and b:
        return str(int(a) + int(b))
    elif a and (not b):
        return a
    elif not a and b:
        return b
    else:
        return '0'
