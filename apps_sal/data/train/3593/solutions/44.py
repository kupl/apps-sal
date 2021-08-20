def capitalize(x, a):
    b = []
    for (i, e) in enumerate(x):
        if i in a:
            b += e.upper()
        else:
            b += e
    return ''.join(b)
