def merge(*dicts):
    keys = set([key for d in dicts for key in d])
    return {key: [d[key] for d in dicts if key in d] for key in keys}
