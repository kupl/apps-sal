def repeat_str(repeat, string):
    x = string
    for i in range(repeat - 1):
        string = string + x
    return string
