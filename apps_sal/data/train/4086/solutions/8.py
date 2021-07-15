def first_non_consecutive(arr):
    pre=arr[0]-1
    for e in arr:
        if e-pre!=1:
            return e
        pre=e
    return

