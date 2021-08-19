def no_space(x):
    z = ''
    for i in range(len(x)):
        if x[i] != ' ':
            z += x[i]
    return z
