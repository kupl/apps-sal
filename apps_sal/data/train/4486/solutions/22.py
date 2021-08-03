def repeat_it(string, n):
    if not isinstance(string, str):
        return "Not a string"
    s = ""
    for i in range(n):
        s += string
    return s
