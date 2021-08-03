def twos_difference(arr):
    arr = sorted(arr)
    b = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] - arr[i] == 2:
                b.append((arr[i], arr[j]))
    return b
