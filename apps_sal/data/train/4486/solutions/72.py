def repeat_it(string, n):
    try:
        string + " "
    except:
        return "Not a string"

    return string * n
