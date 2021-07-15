def no_space(x):
    s = ""
    for letter in x:
        if letter != ' ':
            s += letter
    return s
