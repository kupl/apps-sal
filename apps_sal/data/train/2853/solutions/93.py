def solve(arr):
    for i in list(arr):
        if arr.count(i)>1:
            arr.remove(i)
    return list(arr)

