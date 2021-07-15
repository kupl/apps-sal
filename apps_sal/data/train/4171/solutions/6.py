def no_repeat(string):
    if string.count(string[0]) == 1:
        return string[0]
    else:
        return no_repeat(string.replace(string[0], ''))
