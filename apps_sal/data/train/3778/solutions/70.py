def find_smallest_int(arr, min=None):
    if len(arr) == 0:
        return min
    elif min == None or arr[0] < min:
        min = arr[0]
    return find_smallest_int(arr[1:], min)
