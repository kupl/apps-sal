def min_value(digits):
    z = ''
    n = digits
    y = []
    for x in n:
        if x in y:
            continue
        y.append(x)
        y.sort()
    for x2 in y:
        z = z + str(x2)
    print(z)
    return int(z)
