def unpack(nested):
    if type(nested) in (tuple, list, set):
        return [flat for value in nested for flat in unpack(value)]
    if type(nested) is dict:
        return [flat for (key, value) in list(nested.items()) for flat in unpack(key) + unpack(value)]
    return [nested]
