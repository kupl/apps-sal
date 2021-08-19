def sum_str(a, b):
    if a == '' and b == '':
        return '0'
    elif a != '' and b != '':
        return str(int(a) + int(b))
    elif a == '':
        return b
    elif b == '':
        return a
