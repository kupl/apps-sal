def find_smallest_int(arr):
    smallest = min(arr)
    for i in arr:
        if i < min(arr):
            smallest = i
        return smallest
