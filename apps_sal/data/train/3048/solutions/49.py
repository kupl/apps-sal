def alternateCase(s):
    listW = list(s)
    for i in range(len(listW)):
        if listW[i].islower():
            listW[i]=listW[i].upper()
        elif listW[i].isupper():
            listW[i]=listW[i].lower()
    return ''.join(listW)
