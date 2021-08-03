def remove_exclamation_marks(s):
    res = ""
    for i in s:
        if not(i == "!"):
            res = res + i

    return res
