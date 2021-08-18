def pick_peaks(arr):
    out = {'pos': [], 'peaks': []}

    for i in range(1, len(arr) - 1):
        plateau_idx = i + 1
        if arr[i - 1] < arr[i] == arr[i + 1]:
            while plateau_idx < len(arr):
                if arr[plateau_idx] == arr[i]:
                    plateau_idx += 1
                else:
                    break
        if plateau_idx < len(arr) and arr[i - 1] < arr[i] > arr[plateau_idx]:
            out['pos'].append(i)
            out['peaks'].append(arr[i])
    return out
