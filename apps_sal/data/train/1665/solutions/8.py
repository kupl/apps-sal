def same_structure_as(a, b):
    return type(a) == type(b) and (len(a) == len(b) and all(map(same_structure_as, a, b))) if type(a) == list else 1
