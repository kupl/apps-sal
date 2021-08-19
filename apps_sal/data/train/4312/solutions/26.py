def pick_peaks(arr):
    pos = []
    for i in range(1, len(arr) - 1):
        next_i = next((n for (n, v) in enumerate(arr[i:]) if v != arr[i]), None)
        if arr[i - 1] < arr[i] and next_i and (arr[i] > arr[i:][next_i]):
            pos.append(i)
    return {'pos': pos, 'peaks': [arr[po] for po in pos]}
