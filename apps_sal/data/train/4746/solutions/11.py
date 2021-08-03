hexa = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}


def fisHex(name):
    print(name)
    hexv = [hexa[i] for i in name.lower() if i in hexa]
    s = 0
    for i in range(0, len(hexv)):
        s = s ^ hexv[i]
    return s
