def two_sort(array):
    array.sort()
    return array[0].replace("", "***").strip("***")
