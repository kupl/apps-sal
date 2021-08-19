def merge_arrays(first, second):
    result = sorted(first + second)
    i = 0
    while i <= len(result) - 2:
        if result[i] == result[i + 1]:
            del result[i]
        else:
            i = i + 1
    return result
