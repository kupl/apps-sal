def repeat_it(string, n):
    if type(string) is not str:
        return "Not a string"
    text = ""
    for i in range(n):
        text += string
    return text
