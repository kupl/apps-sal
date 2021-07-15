def sum_str(a, b):
    if a == '' and b == '':
        return str(0)
    
    if a == '':
        return b
    if b == '':
        return a
    
    return str(int(a) + int(b))
