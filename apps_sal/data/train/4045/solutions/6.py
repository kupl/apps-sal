def number(lines):
    # your code here
    a = []
    for i, c in enumerate(lines, 1):
        str_var = str(i) + ': ' + str(c)  # make sure to add another space
        a.append(str_var)
    return a
