def pick_peaks(arr):
    peaks = {'peaks': [], 'pos': []}
    if len(arr) == 0:
        return peaks
    p = min(arr)
    pos = 0
    for i in range(2, len(arr)):
        if arr[i-1] > arr[i-2] and arr[i-1] >= arr[i]:
            p = arr[i-1]
            pos = i-1
        if arr[i] < p:
            peaks['peaks'].append(p)
            peaks['pos'].append(pos)
            p = min(arr)
            pos = 0
    return peaks
