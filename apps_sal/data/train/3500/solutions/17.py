def remove_exclamation_marks(s):
    if "!" not in s:
        return s
    else:
        s1 = ""
        for caracter in s:
            if caracter != "!":
                s1 += caracter
        return s1
