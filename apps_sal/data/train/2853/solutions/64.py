def solve(arr):
    arr = arr[::-1]
    a = []
    for i in arr:
        if i not in a:
            a.append(i)
    return a[::-1]
