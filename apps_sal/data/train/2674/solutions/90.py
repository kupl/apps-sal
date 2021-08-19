def two_sort(array):
    # your code here
    array.sort()
    return array[0].replace("", "***").strip("***")
