def merge_arrays(*a):
    result = []
    for sublist in a:
        for element in sublist:
            if not (element in result):
                result.append(element)
    return sorted(result)
