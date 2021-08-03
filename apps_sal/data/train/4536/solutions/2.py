def capitals_first(string):
    return ' '.join(sorted((a for a in string.split() if a[0].isalpha()),
                           key=lambda b: b[0].islower()))
