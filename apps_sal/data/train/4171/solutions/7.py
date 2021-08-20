def no_repeat(string):
    return min(string, key=string.count)
