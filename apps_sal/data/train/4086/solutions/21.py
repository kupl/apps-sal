def first_non_consecutive(arr):
    k = arr[0]
    for i in arr:
        if i!=k:
            return i
        k+=1
    return None
