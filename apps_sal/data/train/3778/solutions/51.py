def find_smallest_int(arr):

    print(arr)
    arr.sort()
    print(arr)

    out = arr.pop(0)
    print(out)

    return out
