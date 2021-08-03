def find_smallest_int(arr):

    a = 0
    b = 0

    while b < len(arr):
        if arr[a] <= arr[b]:
            b += 1
        elif arr[a] > arr[b]:
            a += 1

    return arr[a]
