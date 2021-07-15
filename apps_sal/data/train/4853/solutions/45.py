def double_char(s):
    new_string = []
    for i in list(s):
        new_string.append(i+i)
    return "".join(new_string)
