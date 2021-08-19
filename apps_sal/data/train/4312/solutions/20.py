def pick_peaks(arr):
    lastind = -1
    pos = list()
    peaks = list()
    status = 'init'
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            status = 'rising'
            lastind = i
        elif arr[i] < arr[i - 1]:
            if status == 'rising':
                pos.append(lastind)
                peaks.append(arr[i - 1])
                status = 'lol'
    return {'pos': pos, 'peaks': peaks}
