def capitalize(s):
    new1 = ""
    new2 = ""
    for i in range(len(s)):
        if i%2 == 0:
            new1 += s[i].upper()
            new2 += s[i]
        else:
            new1 += s[i]
            new2 += s[i].upper()
    return [new1, new2]
