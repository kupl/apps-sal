def pick_peaks(arr):
    a = []
    b = []
    for i in range(1, len(arr) - 1):
        for l in range(i, len(arr) - 1):
            if arr[l + 1] > arr[i]:
                break
            if arr[l + 1] < arr[i]:
                if arr[i - 1] < arr[i] and arr[i + 1] <= arr[i]:
                    a.append(i)
                    b.append(arr[i])
                    break
    return {"pos": a, "peaks": b}
