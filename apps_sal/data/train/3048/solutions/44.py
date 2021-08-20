def alternateCase(s=''):
    print(s)
    listl = list(s)
    n = len(s)
    i = 0
    while i < n:
        if s[i].isupper() == True:
            print(s[i])
            letra = s[i].lower()
            print(letra)
            listl[i] = letra
            print(listl)
            s = ''.join(listl)
            print(s)
        elif s[i].islower() == True:
            print(s[i])
            letra = s[i].upper()
            print(letra)
            listl[i] = letra
            print(listl)
            s = ''.join(listl)
            print(s)
        i += 1
    return s
