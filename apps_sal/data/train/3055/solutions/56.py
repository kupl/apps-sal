def sum_str(a, b):
    if a and b:
        return str(int(a) + int(b))
    elif a or b:
        return a + b
    else:
        return '0'
