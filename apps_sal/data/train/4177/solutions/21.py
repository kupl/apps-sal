def men_from_boys(arr):
    arr = list(set(arr))
    a = []
    b = []
    arr.sort()
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            a.append(arr[i])
        else:
            b.insert(0, arr[i])
    return a + b
