def string_parse(string):

    if not isinstance(string, str):
        return "Please enter a valid string"
    if len(string) == 0:
        return ""
    Di = {}
    text = ""
    f = 0
    i = 0
    f2 = 0
    for i in range(len(string) - 1):
        Di.setdefault(string[i], 0)
        text += string[i]
        Di[string[i]] += 1

        if not f and Di[string[i]] >= 2 and string[i] == string[i + 1]:
            text += "["
            f = 1
        if f and Di[string[i]] >= 2 and string[i] != string[i + 1]:
            text += "]"
            f = 0
            f2 = 1
        if not f and string[i] != string[i + 1]:
            Di[string[i]] = 0

    text += string[-1]
    if f:
        text += "]"
    return text
