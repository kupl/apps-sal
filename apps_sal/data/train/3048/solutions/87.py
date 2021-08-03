def alternateCase(s):
    new_s = []
    for char in s:
        if char.isupper():
            new_s.append(char.lower())
        else:
            new_s.append(char.upper())

    return "".join(new_s)
