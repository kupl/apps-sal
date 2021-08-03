def pick_peaks(arr):
    pospeaks = {"pos": [], "peaks": []}

    for i in range(1, len(arr) - 1):
        lowerbefore = arr[i - 1] < arr[i]
        lowerafter = False
        for j in arr[i:]:
            if j == arr[i]:
                continue
            elif j < arr[i]:
                lowerafter = True
                break
            elif j > arr[i]:
                break
        if lowerbefore and lowerafter:
            pospeaks["pos"].append(i)
            pospeaks["peaks"].append(arr[i])

    return pospeaks
