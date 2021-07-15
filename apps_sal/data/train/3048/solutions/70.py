def alternateCase(s):
    stringy = ''
    for i in s:
        if i.islower():
            stringy += i.upper()
        elif i.isupper():
            stringy += i.lower()
        else:
            stringy += i
    return stringy
