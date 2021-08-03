def sum_str(a, b):
    x = int(a) if a.isnumeric() else 0
    y = int(b) if b.isnumeric() else 0
    return str(x + y)
