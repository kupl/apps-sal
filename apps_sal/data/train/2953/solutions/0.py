def numericals(s):
    dictio = {}
    t = ""
    for i in s:
        dictio[i] = dictio.get(i, 0) + 1
        t += str(dictio[i])
    return t
