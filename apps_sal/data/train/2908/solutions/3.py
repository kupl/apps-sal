def flatten(dictionary, prefix=[]):
    res = {}
    for key in dictionary.keys():
        if isinstance(dictionary[key], dict) and dictionary[key]:
            res.update(flatten(dictionary[key], prefix + [key]))
        else:
            res["/".join(prefix + [key])] = dictionary[key] or ''
    return res
