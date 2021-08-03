def find_difference(a, b):
    vola = 1
    for x in a:
        vola *= x
    volb = 1
    for x in b:
        volb *= x
    return abs(vola - volb)
