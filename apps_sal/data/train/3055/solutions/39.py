def sum_str(a, b):
    if a and b != '':
        return str(int(a)+int(b))
    elif a == '' and b != '':
        return b
    elif b == '' and a != '':
        return a
    else: return '0'
