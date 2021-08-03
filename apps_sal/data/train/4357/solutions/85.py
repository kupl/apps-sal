def nth_smallest(arr, pos):
    arr.sort()
    count = 1
    for x in arr:
        if count == pos:
            return x
        else:
            count += 1
