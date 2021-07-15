def sum_str(a, b):
    if a and b:
        return str(int(a) + int(b))
    if not a and not b:
        return '0'
    if not a:
        return b
    return a

