def dominator(arr):
    return next((x for x in set(arr) if arr.count(x) > len(arr)/2),-1)
