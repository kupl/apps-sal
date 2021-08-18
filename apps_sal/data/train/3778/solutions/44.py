def find_smallest_int(arr):
    smallest = None
    for n in arr:
        if smallest == None:
            smallest = n
        else:
            smallest = min(smallest, n)
    return smallest
