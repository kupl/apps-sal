def find_smallest_int(arr):
    smallestInt = arr[0]
    for var in arr:
        if var < smallestInt:
            smallestInt = var
    return smallestInt
