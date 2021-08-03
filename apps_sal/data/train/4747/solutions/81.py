def repeat_str(count, string):
    str = string
    for count in range(0, count - 1):
        string = string.__add__(str)
    return string


print(repeat_str(4, 'a'))
