def no_ifs_no_buts(a, b):
    result = {a == b: 'equal to', a < b: 'smaller than', a > b: 'greater than'}[True]
    return f'{a} is {result} {b}'
