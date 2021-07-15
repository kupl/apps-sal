def sum_str(a, b):
    if a=='' and b=='':
        return '0'
    if a=='':
        return str(int(b))
    if b=='':
        return str(int(a))
    else:
        return str(int(a)+int(b))
