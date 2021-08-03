def find_smallest_int(arr):

    lowest = arr[0]
    for value in arr:
        if lowest > value:
            lowest = value
    return lowest
