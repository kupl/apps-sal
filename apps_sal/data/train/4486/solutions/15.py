def repeat_it(string, n):
    if (n == 0):
        return ''
    return string * n if type(string) == str else 'Not a string'
