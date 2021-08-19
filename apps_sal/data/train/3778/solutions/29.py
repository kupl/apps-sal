def find_smallest_int(arr):
    # Code here
    smallest = 1000000
    for i in range(0, len(arr), 1):
        if arr[i] < smallest:
            smallest = arr[i]
            arr.append(smallest)
    return arr[-1]
