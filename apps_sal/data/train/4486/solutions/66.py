def repeat_it(string, n):
    if type(string) == int or string == {} or string == [] or (string == 1):
        return 'Not a string'
    else:
        return string * n
