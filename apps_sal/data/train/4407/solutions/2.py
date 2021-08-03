def no_ifs_no_buts(a, b):
    d = {a < b: 'smaller than', a == b: 'equal to', a > b: 'greater than'}
    return f'{a} is {d[True]} {b}'
