def pick_peaks(arr):
    result = {'pos': [], 'peaks': []}
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            result['pos'].append(i)
            result['peaks'].append(arr[i])
        elif arr[i] > arr[i - 1] and arr[i] == arr[i + 1]:
            for k in range(i + 2, len(arr)):
                if arr[i] > arr[k]:
                    result['pos'].append(i)
                    result['peaks'].append(arr[i])
                    break
                elif arr[k] > arr[i]:
                    break
    return result
