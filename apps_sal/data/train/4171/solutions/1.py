def no_repeat(string):
    return [x for x in string if string.count(x) == 1][0]
