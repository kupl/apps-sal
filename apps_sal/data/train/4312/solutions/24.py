def pick_peaks(arr):
    ppos = [i for (i, x) in enumerate(arr) if i == 0 or arr[i - 1] != arr[i]]
    pos = [ppos[i] for i in range(1, len(ppos) - 1) if arr[ppos[i]] > arr[ppos[i - 1]] and arr[ppos[i]] > arr[ppos[i + 1]]]
    return {'pos': pos, 'peaks': [arr[i] for i in pos]}
