def solve(arr):
    item = arr.pop()
    while(-item in arr):
        arr.remove(-item)
        item = arr.pop()
    return item
