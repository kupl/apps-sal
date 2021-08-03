def solve(arr):
    for j in reversed(arr):
        if arr.count(j) != 1:
            arr.remove(j)
    return arr
