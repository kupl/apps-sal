def merge_arrays(first, second):
    if isinstance(first, dict) or isinstance(second, dict):
        return sorted(dict(dict.fromkeys(list(first.keys()) + list(second.keys()))))
    return sorted(dict(dict.fromkeys(first + second)))
