def compound_array(a, b):
    r = []
    while a or b:
        r += a[:1] + b[:1]
        (a, b) = (a[1:], b[1:])
    return r
