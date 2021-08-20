def sum_str(a, b):
    return '0' if a == '' and b == '' else str(a) if b == '' else str(b) if a == '' else str(int(a) + int(b))
