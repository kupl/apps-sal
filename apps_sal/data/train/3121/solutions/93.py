def solve(arr):
    for i in arr:
        if i in arr and i * -1 not in arr:
            return i

