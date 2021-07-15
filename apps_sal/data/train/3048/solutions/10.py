def alternateCase(s):
    string = ""
    for char in s:
        if char.islower():
            string += char.upper()
        else:
            string += char.lower()
    return string

