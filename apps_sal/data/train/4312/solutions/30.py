def pick_peaks(arr):
    pos = []
    peaks = []
    i = 1
    while i < len(arr) - 1:
        if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            pos.append(i)
            peaks.append(arr[i])
        elif arr[i - 1] < arr[i] < arr[i + 1]:
            pass
        elif arr[i - 1] < arr[i]:
            if i < len(arr):
                for j in range(i, len(arr) - 1):
                    if arr[j] == arr[j + 1]:
                        continue
                    elif arr[j] < arr[j + 1]:
                        i = j - 1
                        break
                    elif arr[j] > arr[j + 1]:
                        pos.append(i)
                        peaks.append(arr[i])
                        i = j - 1
                        break
        i += 1

    return {'pos': pos, 'peaks': peaks}
