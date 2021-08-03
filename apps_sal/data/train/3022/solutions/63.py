def two_highest(arg1):
    arg1 = list(set(arg1))
    terminos = []
    if len(arg1) > 0:
        terminos.append(arg1[0])
        for x in arg1:
            if x > terminos[0]:
                terminos[0] = x
        arg1.remove(terminos[0])
    if len(arg1) > 0:
        terminos.append(arg1[0])
        for x in arg1:
            if x > terminos[1]:
                terminos[1] = x
    return terminos
