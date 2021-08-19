def no_space(x):
    secondary = list()
    for i in x:
        if i != ' ':
            secondary.append(i)
    return ''.join(secondary)
