def find_smallest_int(arr):
    for small in arr:
        if small == arr[0]:
            low = small
        else:
            if low > small:
                low = small
    return low
