def remove_exclamation_marks(s):
    a = str()
    for i in s:
        if i != "!":
            a += i
    return a
