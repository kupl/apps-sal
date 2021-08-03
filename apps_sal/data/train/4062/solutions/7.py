def solve(arr):
    a = set()
    for x in range(len(arr)):
        if arr != []:
            a.add(max(arr))
            arr = arr[(arr.index(max(arr))) + 1:]

    return sorted(list(a), reverse=True)
