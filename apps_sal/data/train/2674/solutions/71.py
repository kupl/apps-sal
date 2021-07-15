def two_sort(array):
    array.sort()
    a = ""
    for x in range(len(array[0])-1):
        a += array[0][x] + "***"
    return a + array[0][-1]
