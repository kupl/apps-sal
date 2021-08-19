def sum_str(a='0', b='0'):
    if a == '':
        a = '0'
    if b == '':
        b = '0'
    c = int(a) + int(b)
    return f'{c}'
