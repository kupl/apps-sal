def alternateCase(s):
    output = ''
    for c in s:
        if c.isupper():
            output += c.lower()
        elif c.islower():
            output += c.upper()
        else:
            output += c
    return output
