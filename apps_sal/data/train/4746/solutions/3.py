from functools import reduce


def fisHex(name):
    hex = ['a', 'b', 'c', 'd', 'e', 'f']
    hexFish = []
    for i in name.lower():
        if i in hex:
            hexFish.append(i)
    hexList = [int(x, 16) for x in hexFish]
    if hexList != []:
        hexValue = hexList[0]
    else:
        return 0
    hexValue = reduce(lambda x, y: x ^ y, hexList)
    return hexValue
