def sum_str(a, b):
    if not a.isnumeric():
        a = 0
    if not b.isnumeric():
        b = 0
    return str(int(a) + int(b))
