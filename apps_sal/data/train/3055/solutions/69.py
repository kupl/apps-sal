def sum_str(a, b):
    if b == '' and a == '':
        return '0'
    if a == '':
        return b
    if b == '':
        return a
    else:
        return str(int(a) + int(b))
