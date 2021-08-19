def no_space(x):
    str = []
    for char in x:
        if char != ' ':
            str.append(char)
    return ''.join(str)
