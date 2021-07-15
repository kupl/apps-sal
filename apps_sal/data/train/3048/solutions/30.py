def alternateCase(s):
    l=[]
    for i in s:
        if i == " " or i == "":
            l.append(i)
        elif i.isupper():
            l.append(i.lower())
        elif i.islower():
            l.append(i.upper())
    return "".join(l)
