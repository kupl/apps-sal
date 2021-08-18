def isValid(formula):
    material = [m + 1 in formula for m in range(8)]
    r1 = not (material[0] and material[1])
    r2 = not (material[2] and material[3])
    r3 = not (material[4] ^ material[5])
    r4 = material[6] or material[7]
    return r1 and r2 and r3 and r4
