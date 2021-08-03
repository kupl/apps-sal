def flatten(d):
    result = []
    for key in d:
        if isinstance(d[key], str):
            result.append((key, d[key]))
        elif len(d[key]) == 0:
            result.append((key, ""))
        else:
            for key2, value2 in list(flatten(d[key]).items()):
                result.append((key + "/" + key2, value2))
    return dict(result)
