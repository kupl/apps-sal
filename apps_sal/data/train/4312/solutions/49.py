def pick_peaks(arr):
    l = []
    t = []
    for i in range(len(arr) - 2):
        if arr[i + 1] > arr[i]:
            k = 0
            while k + i + 1 < len(arr):
                if arr[k + i + 1] > arr[i + 1]:
                    break
                if arr[k + i + 1] < arr[i + 1]:
                    l.append(arr[i + 1])
                    t.append(i + 1)
                    break
                k = k + 1
    return {'pos': t, 'peaks': l}
