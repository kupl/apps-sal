def sum_str(a, b):
    if a and b:
        return str(int(a) + int(b))
    elif a == '':
        if b:
            return b
        else:
            return '0'
    else:
        return a
