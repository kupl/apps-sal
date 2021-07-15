def pick_peaks(arr):
    pos = []
    peaks = []
    i = 1
    while i < len(arr) - 1:
        if arr[i - 1] < arr[i]:
            j = i + 1
            while j < len(arr):
                print(arr[i], arr[j])
                if arr[i] > arr[j]:
                    pos.append(i)
                    peaks.append(arr[i])
                    break
                elif arr[i] == arr[j]:
                    j += 1
                else:
                    break
        i += 1
    return {"pos": pos, "peaks": peaks}
