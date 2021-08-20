def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        (array[i], array[m]) = (array[m], array[i])


def nth_smallest(arr, pos):
    if pos <= 0 or arr == []:
        return 'error'
    sel_sort(arr)
    return arr[pos - 1]
