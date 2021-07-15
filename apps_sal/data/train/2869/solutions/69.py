def distinct(seq):
    liste = []
    for a in seq:
        if not a in liste:
            liste.append(a)
    return liste
