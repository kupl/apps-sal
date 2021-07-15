def alternateCase(s):
    text = ""
    for i in s:
        if i.islower():
            text += i.upper()
        else:
            text += i.lower()
    return text
