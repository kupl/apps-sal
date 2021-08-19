def pick_peaks(arr):
    result = {'pos': [], 'peaks': []}
    for (pos, val) in enumerate(arr):
        if pos == 0 or pos == len(arr) - 1:
            continue
        if arr[pos + 1] > val:
            continue
        if arr[pos - 1] == val:
            continue
        if arr[pos + 1] == val and arr[pos - 1] < val:
            for i in range(pos + 1, len(arr)):
                if arr[i] == val:
                    continue
                elif arr[i] > val:
                    break
                else:
                    result['pos'].append(pos)
                    result['peaks'].append(val)
                    break
            continue
        if arr[pos - 1] < val:
            result['pos'].append(pos)
            result['peaks'].append(val)
    return result
