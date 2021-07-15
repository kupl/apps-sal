def near_flatten(nested):
    result = []
    for item in nested:
        if type(item[0]) == list:
            result.extend(near_flatten(item))
        else:
            result.append(item)
    return sorted(result, key=lambda l: l[0])
