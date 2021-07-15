def repeat_it(string,n):
    a = ""
    if isinstance(string, str):
        for i in range(0, n):
            a = a + string
    else:
        return "Not a string"
    return a
