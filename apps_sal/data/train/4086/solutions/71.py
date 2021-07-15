def first_non_consecutive(arr):
    i = arr.pop(0)
    for item in arr:
        i += 1
        if item != i:
            return item 
    return None
