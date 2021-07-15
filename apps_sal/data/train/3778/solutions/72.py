def find_smallest_int(arr):
    smallest = arr[0]
    for n in arr[1:]:
        if n < smallest:
            smallest = n
    return smallest
