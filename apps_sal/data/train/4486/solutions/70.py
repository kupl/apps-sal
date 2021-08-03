def repeat_it(string, n):
    if isinstance(string, str):
        final = ""
        for i in range(n):
            final += string
        return final
    else:
        return "Not a string"
