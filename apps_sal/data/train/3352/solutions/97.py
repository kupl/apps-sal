def find_longest(arr):

    copy = list(arr)
    i = 0
    while i < len(copy):
        copy[i] = len(str(copy[i]))
        i = i + 1
    maximum = max(copy)
    index = copy.index(maximum)

    return arr[index]
