def filter_homogenous(arrays):
    return[a for a in arrays if len(set(map(type, a))) == 1]
