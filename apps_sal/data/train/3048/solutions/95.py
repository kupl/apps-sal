def alternateCase(s):
    text = ''
    for i in range(len(s)):
        if s[i].isupper() == True:
            text = text + s[i].lower()
        else:
            text = text + s[i].upper()
    return text
