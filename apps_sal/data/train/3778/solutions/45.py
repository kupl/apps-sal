def find_smallest_int(arr):
    smallest = 999999999999999999999999999999999999999999999999999
    for item in arr:
        if int(item) < smallest:
            smallest = item
    return smallest
