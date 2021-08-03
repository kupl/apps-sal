def pick_peaks(arr):
    result = {'pos': [], 'peaks': []}
    increasing = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            increasing = True
            tmpk = arr[i]
            tmpindx = i
        elif arr[i] < arr[i - 1]:
            if increasing:
                result['pos'].append(tmpindx)
                result['peaks'].append(tmpk)
                increasing = False
    return result
