def distinct(seq):
    result = []
    uniques = {i:True for i in set(seq)}
    for object in seq:
        if uniques[object]:
            result.append(object)
            uniques[object] = False
    return result
