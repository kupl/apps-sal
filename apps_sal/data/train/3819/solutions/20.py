def smash(words):
    s = ""
    for i,j in enumerate(words):
        if i==0:
            s += j
        else:
            s += " "+j
    return s
