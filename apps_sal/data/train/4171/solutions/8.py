def no_repeat(string):
    for c in string:
        if len(string.split(c)) == 2:
            return c
