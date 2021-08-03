def repeat_str(repeat, string):
    s = string
    for i in range(1, repeat):
        s = s + string
    return s
