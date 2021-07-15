def capitalize(s):
    new = ""
    new1=""
    out = []
    for i in range(len(s)):
        if i%2==0:
            new+=s[i].upper()
        else:
            new+=s[i]
    out.append(new)
    for i in range(len(s)):
        if i%2==0:
            new1+=s[i]
        else:
            new1+=s[i].upper()
    out.append(new1)
    return out

