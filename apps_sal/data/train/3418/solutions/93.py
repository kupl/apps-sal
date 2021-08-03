def reverse_list(l):
    result = []
    i = len(l)
    while i > 0:
        i -= 1
        result.append(l[i])
    return result
