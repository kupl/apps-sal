def trouble(array, target):
    i = 0
    while i < len(array) - 1:
        if array[i] + array[i + 1] == target:
            del array[i + 1]
        else:
            i += 1
    return array
