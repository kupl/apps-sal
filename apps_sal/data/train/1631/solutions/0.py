def snail(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in range((size + 1) // 2):
            for x in range(n, size - n):
                ret.append(array[n][x])
            for y in range(1 + n, size - n):
                ret.append(array[y][-1 - n])
            for x in range(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            for y in range(2 + n, size - n):
                ret.append(array[-y][n])
    return ret
