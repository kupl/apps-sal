def alternateCase(s):
    s = [letter for letter in s]
    for i in range(len(s)):
        if s[i] == s[i].upper():
            s[i] = s[i].lower()
        else:
            s[i] = s[i].upper()
    return ''.join(s)
