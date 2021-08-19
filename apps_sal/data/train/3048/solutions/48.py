def alternateCase(string):
    res = ''
    for char in string:
        if char.lower() == char:
            res += char.upper()
        else:
            res += char.lower()
    return res
