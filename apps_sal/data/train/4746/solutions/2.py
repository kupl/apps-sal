def fisHex(name):
    hexx = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    name = name.lower()
    result = 0
    for i in name:
        if i in hexx:
            result = result ^ hexx[i]
    return result
