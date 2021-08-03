def repeat_it(string, n):
    if not string or isinstance(string, int):
        return "Not a string"
    else:
        return string * n
