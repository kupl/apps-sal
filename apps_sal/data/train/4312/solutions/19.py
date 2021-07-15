def pick_peaks(arr):
    res = {'pos': [], 'peaks': []}
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] > arr[[n for n in range(i, len(arr)) if arr[n] != arr[i] or n == len(arr) - 1][0]]:
            res.update({'pos': res.get('pos') + [i]})
            res.update({'peaks': res.get('peaks') + [arr[i]]})
    return res
