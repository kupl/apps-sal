def no_space(x):
    tmp = ''
    for char in x:
        if char is not ' ':
            tmp += char
    return tmp

