def pick_peaks(arr):
    result = {'pos': [], 'peaks': []}
    flagIndex = -1
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            result['pos'].append(i)
            result['peaks'].append(arr[i])
        elif arr[i - 1] < arr[i] == arr[i + 1]:
            flagIndex = i
        elif flagIndex != -1:
            if arr[i] > arr[i + 1]:
                result['pos'].append(flagIndex)
                result['peaks'].append(arr[flagIndex])
                flagIndex = -1
            elif arr[i] < arr[i + 1]:
                flagIndex = -1
    return result
