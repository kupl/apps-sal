def find_smallest_int(arr):
    n = len(arr)
    smallest = arr[0]
    for i in range(n):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest
         

