def no_repeat(string):
    for i in string:
        if string.index(i) == len(string) - string[::-1].index(i) - 1:
            return i
