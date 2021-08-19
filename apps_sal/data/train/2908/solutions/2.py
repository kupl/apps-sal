def flatten(d):
    result = {}
    for (key, value) in d.items():
        if value and isinstance(value, dict):
            for (k, v) in flatten(value).items():
                result[key + '/' + k] = v
        else:
            result[key] = value or ''
    return result
