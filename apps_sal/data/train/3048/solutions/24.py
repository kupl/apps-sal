def alternateCase(s):
    switched_str = ''
    for c in s:
        if c.islower():
            switched_str += c.upper()
        else:
            switched_str += c.lower()
    return switched_str
