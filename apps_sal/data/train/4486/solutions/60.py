def repeat_it(string, n):
    return string * n if string.__class__ == str else 'Not a string'
