def repeat_it(string, n):
    print(string, n)
    return string * n if type(string) == str else 'Not a string'
