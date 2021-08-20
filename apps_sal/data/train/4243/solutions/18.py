def find_average(array):
    if len(array) == 0:
        return 0
    i = 0
    tot = 0
    while i < len(array):
        tot = tot + array[i]
        i += 1
    return tot / len(array)
