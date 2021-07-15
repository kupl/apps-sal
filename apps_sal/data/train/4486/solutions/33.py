def repeat_it(string,n):
    if isinstance(string, str):
        a = ""
        for i in range (1, n + 1):
            a += string
        return a
    else:
        return "Not a string"
