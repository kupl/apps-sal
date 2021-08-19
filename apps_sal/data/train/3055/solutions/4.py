def sum_str(a, b):
    if a == '' and b == '':
        return '0'
    if b == '':
        return a
    if a == '':
        return b
    if a == '' and b == '':
        return '0'
    return str(int(a) + int(b))
    pass
