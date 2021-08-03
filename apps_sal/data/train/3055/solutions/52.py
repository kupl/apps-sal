def sum_str(a, b):
    if a.isdigit() and b.isdigit():
        return str(int(a) + int(b))
    elif a is '' and b is '':
        return "0"
    return a + b
