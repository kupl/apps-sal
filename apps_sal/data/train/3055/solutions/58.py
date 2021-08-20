def sum_str(a, b):
    if a.isdigit() == False:
        a = 0
    if b.isdigit() == False:
        b = 0
    a = int(a)
    b = int(b)
    return str(a + b)
