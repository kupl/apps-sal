def sum_str(a, b):
    if a and b:
        return str(int(a) + int(b))
    else:
        if a:
            return a
        if b:
            return b
        else:
            return '0'
