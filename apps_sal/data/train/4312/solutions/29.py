def pick_peaks(arr):
    out = {}
    i, wait_pick, temp_pick = 1, 0, 0
    while i < len(arr) - 1:
        if arr[i] == arr[i+1] and arr[i] > arr[i-1]:
            temp_pick = i
            wait_pick = 1
            i += 1   
            continue
        if wait_pick == 1:
            if arr[i] > arr[i+1]:
                out[temp_pick] = arr[temp_pick]
                wait_pick = 0
            elif arr[i] < arr[i+1]:
                wait_pick = 0
            i += 1
        else:
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                out[i] = arr[i]
            i += 1
    return {"pos": list(out.keys()), "peaks": list(out.values())}
