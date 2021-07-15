def first_non_consecutive(arr):
    for i, e in enumerate(arr):
        if i == len(arr)-1: return None
        elif e+1 != arr[i+1]: return arr[i+1]

