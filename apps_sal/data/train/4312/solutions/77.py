def pick_peaks(arr):
    pos, peaks = [], []

    for i in range(1, len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            k = i
            while k < len(arr) - 2 and arr[k] == arr[k + 1]:
                k += 1
            if arr[i - 1] < arr[i] and arr[i] > arr[k + 1]:
                pos.append(i)
                peaks.append(arr[i])
    
    return {"pos": pos, "peaks": peaks}

