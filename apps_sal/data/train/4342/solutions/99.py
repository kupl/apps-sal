def no_space(x):
    for i in range(5):
        spaces = i * ' '
        x = x.replace(spaces, '')
    return x
