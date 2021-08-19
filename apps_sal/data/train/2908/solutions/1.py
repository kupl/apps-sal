def flatten(dictionary):
    result = {}
    for (k, v) in dictionary.items():
        if v == {}:
            result[k] = ''
        elif isinstance(v, dict):
            for (l, w) in flatten(v).items():
                result[k + '/' + l] = w
        else:
            result[k] = v
    return result
