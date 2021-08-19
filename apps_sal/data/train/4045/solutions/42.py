def number(lines):
    x = lines
    y = []
    z = 0
    for i in range(len(lines)):
        z += i
        y.append(str(i + 1) + ':' + ' ' + x[i])
    return y
