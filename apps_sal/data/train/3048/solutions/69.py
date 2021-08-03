def alternateCase(s):
    lst = []
    for i in s:
        if i == i.upper():
            lst.append(i.lower())
        else:
            lst.append(i.upper())
    return ''.join(lst)
