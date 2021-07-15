def two_sort(array):
    array.sort()
    n = ""
    for i in range(0, len(array[0])):
        if i == len(array[0])-1:
            n = n + array[0][i]
            break
        n = n + array[0][i] + "***"
    return n

