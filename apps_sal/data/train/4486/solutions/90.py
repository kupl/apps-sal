def repeat_it(string, n):
    tipus = type(string)
    print(("==>> ", string, n, tipus))
    if tipus == str:
        output = string * n
        return output
    else:
        return "Not a string"
