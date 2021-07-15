def repeat_str(repeat, string):
    new_str = ''
    while repeat > 0:
        new_str += string
        repeat -= 1
    return new_str
