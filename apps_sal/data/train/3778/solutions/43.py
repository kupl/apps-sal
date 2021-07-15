def find_smallest_int(arr):
    n = len(arr)
    minimum = arr[0]
    for i in range(1, n):
        if arr[i] < minimum:
            minimum = arr[i]
    return minimum
    # Code here

