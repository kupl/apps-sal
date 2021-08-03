def sum_str(a, b):
    avar = 0
    bvar = 0

    if a.isdigit():
        avar = float(a)
    if b.isdigit():
        bvar = float(b)

    return str(int(avar + bvar))
