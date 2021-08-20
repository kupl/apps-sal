def alternateCase(s):
    new_string = ''
    for a in s:
        if a.isupper() == True:
            new_string += a.lower()
        elif a.islower() == True:
            new_string += a.upper()
        elif a.isspace() == True:
            new_string += a
    return new_string
