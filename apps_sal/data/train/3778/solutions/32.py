def find_smallest_int(arr):
    number = arr[0]
    for nb in arr:
        if nb < number:
            number = nb
    return number
