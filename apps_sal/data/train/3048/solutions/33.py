def alternateCase(s):
    lst = []
    for x in s:
        if x.islower():
            lst.append(x.upper())
        elif x.isupper():
            lst.append(x.lower())
        else:
            lst.append(x)
    x = ''.join(lst)
    return x
