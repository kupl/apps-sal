def remove_exclamation_marks(s):
    r = list(s)
    for char in s:
        if char == "!":
            r.remove(char)
    string = ''
    for i in r:
        string += i
    return string
