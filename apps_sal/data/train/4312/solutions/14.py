def pick_peaks(arr):
    (i, pos) = (len(arr) - 2, [])
    while i > 0:
        while i > 0 and arr[i + 1] >= arr[i]:
            i -= 1
        while i > 0 and arr[i + 1] <= arr[i]:
            i -= 1
            if arr[i + 1] > arr[i]:
                pos.append(i + 1)
    return {'peaks': [arr[i] for i in pos[::-1]], 'pos': pos[::-1]}
