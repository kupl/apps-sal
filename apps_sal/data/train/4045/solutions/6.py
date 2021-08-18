def number(lines):
    a = []
    for i, c in enumerate(lines, 1):
        str_var = str(i) + ': ' + str(c)
        a.append(str_var)
    return a
