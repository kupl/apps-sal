def sum_str(a, b):
    if len(b) == 0:
        b = str(0)
    if len(a) == 0:
        a = str(0)
    return str(int(a) + int(b))
