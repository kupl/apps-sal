def no_space(x):
    str_char = ''
    for i in range(len(x)):
        if x[i] == ' ':
            continue
        else:
            str_char = str_char + x[i]
    return str_char
