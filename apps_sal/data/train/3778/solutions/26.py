def find_smallest_int(arr):
    smol = arr[0]
    for i in arr:
        if smol > i:
            smol = i
    return smol
