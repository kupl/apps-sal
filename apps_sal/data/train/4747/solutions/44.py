def repeat_str(repeat, string):
    other = string
    for i in range(repeat-1):
        string += other
    return string
