def pick_peaks(arr):
    posPeaks = {'pos': [], 'peaks': []}
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1]:
            if arr[i] > arr[i + 1]:
                posPeaks['pos'].append(i)
                posPeaks['peaks'].append(arr[i])
            if arr[i] == arr[i + 1]:
                for x in range(i + 2, len(arr)):
                    if arr[x] < arr[i]:
                        posPeaks['pos'].append(i)
                        posPeaks['peaks'].append(arr[i])
                        break
                    if arr[x] > arr[i]:
                        break
    return posPeaks
