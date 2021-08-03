def sum_str(a, b):
    if a and b:
        return str(int(a) + int(b))
    elif a:
        return str(a)
    elif b:
        return str(b)
    else:
        return '0'
