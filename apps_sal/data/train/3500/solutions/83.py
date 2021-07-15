def remove_exclamation_marks(s):
    toprint = ""
    for char in s:
        if char != "!":
            toprint += char
    print (toprint)
    return toprint

