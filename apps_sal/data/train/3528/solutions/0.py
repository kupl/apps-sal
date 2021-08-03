def compound_array(a, b):
    x = []
    while a or b:
        if a:
            x.append(a.pop(0))
        if b:
            x.append(b.pop(0))
    return x
