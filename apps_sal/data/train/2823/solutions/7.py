def duplicates(array):
    result = []

    for i, v in enumerate(array):
        if v in array[:i] and v not in result:
            result.append(v)

    return result
