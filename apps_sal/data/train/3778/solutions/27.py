def find_smallest_int(arr):
    print(arr)
    smallest = arr[0]
    for x in arr:
        if x < smallest:
            smallest = x
    return smallest
