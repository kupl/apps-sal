def lowercase_count(strng):

    dgu = []
    rwp = []
    pwr = list(str(strng))
    pwr.sort()
    for lower in pwr:
        if lower.islower():
            rwp.append(lower)
    dgu = len(rwp)
    return dgu
