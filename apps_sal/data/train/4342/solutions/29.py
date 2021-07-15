def no_space(x):
    s = ''
    for i in range(len(x)):
        if x[i] == ' ':
            continue
        else:
            s += x[i]
    return s
