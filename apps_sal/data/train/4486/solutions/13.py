def repeat_it(string, n):
    print(type(string))
    return string * n if type(string) is str else 'Not a string'
