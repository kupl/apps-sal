def createDict(keys, values):
    values += [None] * (len(keys) - len(values))
    return dict(zip(keys, values))
