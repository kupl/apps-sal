# option 1
def find_smallest_int(arr):
    arr.sort()
    return arr[0] 

# option 2
    return min(arr)

# option 3
def find_smallest_int(arr):
    smallest = arr[0]
    for item in arr:
        if smallest > item:
            smallest = item
    return smallest


