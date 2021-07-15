def isValid(formula):
    material = [m + 1 in formula for m in range(8)]
    r1 = not (material[0] and material[1])  # material1 and material2 cannot be selected at the same time
    r2 = not (material[2] and material[3])  # material3 and material4 cannot be selected at the same time
    r3 = not (material[4] ^ material[5])  # material5 and material6 must be selected at the same time
    r4 = material[6] or material[7]  # material7 or material8 must be selected(at least one, or both)
    return r1 and r2 and r3 and r4

