def repeat_it(string, n):
    try:
        if len(string) > 0:
            return string * n
        else:
            return 'Not a string'
    except TypeError:
        return 'Not a string'
