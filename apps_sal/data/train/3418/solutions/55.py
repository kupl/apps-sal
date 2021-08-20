def reverse_list(l):
    result = []
    if len(l) == 0:
        return result
    for item in l[::-1]:
        result.append(item)
    return result
