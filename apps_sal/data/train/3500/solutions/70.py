def remove_exclamation_marks(s):
    ergebnis = ""
    for i in s:
        if i != "!":
            ergebnis += i
    return ergebnis
