def twos_difference(lst):
    result = []
    for elem in lst:
        if elem + 2 in lst:
            result.append((elem, elem + 2))
    result.sort()
    return result
