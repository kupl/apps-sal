def solve(arr):
    arr2 = []
    for i in arr[::-1]:
        if i not in arr2:
            arr2.insert(0, i)
    return arr2
