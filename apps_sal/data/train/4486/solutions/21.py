def repeat_it(string, n):
    return ''.join([string for x in range(n)]) if type(string) is str else 'Not a string'
