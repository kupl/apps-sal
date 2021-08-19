def sum_str(a, b):
    #print(a, b)
    if not a and not b:
        x = 0
        y = 0
    elif not a:
        x = 0
        y = int(b)
    elif not b:
        y = 0
        x = int(a)
    else:
        x = int(a)
        y = int(b)

    return str(x + y)
