def find_smallest_int(arr):
    # Code here
    #initialise first integer as min
    min = arr[0]
    for x in range(1, len(arr)):
        if arr[x] < min:
            min = arr[x]
    return min
