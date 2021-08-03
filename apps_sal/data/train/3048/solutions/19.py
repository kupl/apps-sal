def alternateCase(s):
    copy = list(s)
    for i in range(0, len(s)):
        if(s[i].isupper()):
            copy[i] = s[i].lower()
        elif(s[i].islower()):
            copy[i] = s[i].upper()
        else:
            continue
    return ''.join(copy)
