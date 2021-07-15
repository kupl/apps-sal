def alternateCase(s):
    res = ''
    for i in [i for i in s]:
        if i.isupper() == True:
            res = res + i.lower()
        else:
            res = res + i.upper()
    return res
