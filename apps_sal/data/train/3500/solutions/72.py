def remove_exclamation_marks(s):
    bas = ''
    out = ''
    for i in s:
        if i == "!":
            bas += i
        else:
            out += i
    return out
