def duplicates(array):
    dub = []
    for (i, el) in enumerate(array):
        if i != array.index(el) and el not in dub:
            dub.append(el)
    return dub
