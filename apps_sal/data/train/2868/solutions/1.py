def is_nice(arr):
    return all(x+1 in arr or x-1 in arr for x in arr) and len(arr)>0
