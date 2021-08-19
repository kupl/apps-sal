def solve(arr):
    a2 = []
    for (e, a) in enumerate(arr):
        if a not in arr[e + 1:]:
            a2.append(a)
    return a2
