def createDict(keys, values):
    return {k:(values[i] if i<len(values) else None) for i,k in enumerate(keys)}
