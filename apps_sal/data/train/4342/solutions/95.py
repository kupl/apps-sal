def no_space(x):
    new_string = ''
    for i in range(0, len(x)):
        if x[i] != ' ':
            new_string += x[i]
    return new_string
