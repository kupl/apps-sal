def rad_ladies(text):
    return ''.join((c for c in text if c.isalpha() or c in ' !')).upper()
