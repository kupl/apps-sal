def repeat_it(string, n):
    if type(string) == str:
        return string * n
    elif type(string) != str:
        return "Not a string"
