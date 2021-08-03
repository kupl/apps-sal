def repeat_it(string, n):
    try:
        if type(string) == str:
            return string * n
        else:
            return "Not a string"
    except:
        return "Not a string"
