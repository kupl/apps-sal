def first_non_consecutive(arr):
    for i in range(len(arr)-1):
        if not arr[i]+1 == arr[i+1]: return arr[i+1]
    return None
