def solve(arr):
    dist = {}
    l = len(arr)
    for i in range(l):
        if arr[l - i - 1] in dist.keys():
            arr.pop(l - i - 1)
        else:
            dist[arr[l - i - 1]] = 1
    return arr
