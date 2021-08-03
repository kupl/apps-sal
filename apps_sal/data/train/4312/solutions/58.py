def pick_peaks(arr):
    print(arr)
    obj = {"pos": [], "peaks": []}
    if len(arr) == 0:
        return obj
    upward = True if arr[0] < arr[1] else False
    pos = 1
    plateau = 0

    while pos < len(arr) - 1:
        if upward:
            if arr[pos] == arr[pos + 1]:
                plateau += 1
            elif arr[pos] > arr[pos + 1] and arr[pos] >= arr[pos - 1]:
                obj["pos"].append(pos - plateau)
                obj["peaks"].append(arr[pos])
                upward = False
                plateau = 0
            else:
                plateau = 0
            pos += 1
        else:
            if arr[pos] < arr[pos + 1]:
                upward = True
            pos += 1

    return obj
