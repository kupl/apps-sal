def remove_exclamation_marks(s):
    string = ""
    for x in s:
        if x != "!":
          string = string + x
    return string
