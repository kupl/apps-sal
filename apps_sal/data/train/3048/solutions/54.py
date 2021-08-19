def alternateCase(s):
    s = str(s)
    ergebnis = ''
    for letter in s:
        if letter.isupper():
            ergebnis += letter.lower()
        else:
            ergebnis += letter.upper()
    return ergebnis
