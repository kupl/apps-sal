def find_smallest_int(arr):
    arr.sort()
    return arr[0]

    return min(arr)


def find_smallest_int(arr):
    smallest = arr[0]
    for item in arr:
        if smallest > item:
            smallest = item
    return smallest
