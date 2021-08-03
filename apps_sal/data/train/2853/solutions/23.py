def solve(arr):
    arr2 = []
    for i in range(0, len(arr)):
        f = 0
        for j in range(i + 1, len(arr)):
            if arr[j] == arr[i]:
                f = f + 1
        if f == 0:
            arr2.append(arr[i])
    return arr2
