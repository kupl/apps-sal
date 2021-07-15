def solve(arr):
    ds = []
    for x in arr:
        if arr.count(x) > 1:
            if x not in ds:
                ds.append(x)
            else:
                pass
        else:
            pass
    for x in ds:
        while arr.count(x) > 1:
            arr.remove(x)
    
    return arr
