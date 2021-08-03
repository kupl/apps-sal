def solve(arr):
    list = arr.copy()
    for i in arr:
        if list.count(i) > 1:
            list.remove(i)
    return list
