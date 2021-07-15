def remove_exclamation_marks(s):
    newS = ""
    for letters in s:
        if letters != "!":
            newS += letters
    return newS
