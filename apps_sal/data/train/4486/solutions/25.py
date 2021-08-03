def repeat_it(string, n):
    if string == [] or string == {}:
        return 'Not a string'
    if isinstance(string, int):
        return 'Not a string'
    print(string)
    return string * n
