def repeat_it(string, n):
    try:
        if str(string) == string:
            return string * n
        else:
            return "Not a string"
    except ValueError:
        return string * n
