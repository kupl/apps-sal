def alternateCase(s):
    lst = list()
    for i in s:
        if i.isupper():
            lst.append(i.lower())
        elif i.islower():
            lst.append(i.upper())
        else:
            lst.append(" ")
    return "".join(lst)
