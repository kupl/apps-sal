def find_smallest_int(arr):
    min_number = arr[0]

    for element in arr:
        if element < min_number:
            min_number = element

    return min_number
