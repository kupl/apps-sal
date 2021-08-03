def solve(arr):
    i = 0
    while i < len(arr):
        if arr.count(arr[i]) > 1:
            arr.remove(arr[i])
            i = 0
        else:
            i += 1
    return arr
