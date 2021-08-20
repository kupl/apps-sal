def alternateCase(st):
    string = ''
    for letters in st:
        if letters.isupper():
            string += letters.lower()
        else:
            string += letters.upper()
    return string
