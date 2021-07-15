def sum_str(a, b):
    if a == '' or b == '':
        return '0' if a == '' and b == '' else a if b == '' else b
    return str(int(a) + int(b))
