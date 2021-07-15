def remove_exclamation_marks(s):
    for element in s:
        if element == "!":
            s = s.replace("!", "")
    return s
