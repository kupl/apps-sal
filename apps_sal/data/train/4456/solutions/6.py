def flatten_me(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result

