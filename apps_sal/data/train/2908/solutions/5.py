def flatten(dictionary):
    result = {}
    for k1, v1 in dictionary.items():
        if type(v1) == str:
            result[k1] = v1
        elif v1:
            for k2, v2 in flatten(v1).items():
                result[f"{k1}/{k2}"] = v2
        else:
            result[k1] = ""
    return result
