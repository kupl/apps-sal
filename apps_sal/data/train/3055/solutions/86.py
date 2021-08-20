def sum_str(a, b):
    if a == '' and b == '':
        c = '0'
        return c
    elif a == '' and b != 0:
        return str(b)
    elif b == '' and a != 0:
        return str(a)
    elif b == '' and a == '':
        return 0
    else:
        return str(int(a) + int(b))
