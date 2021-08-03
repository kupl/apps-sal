def pick_peaks(arr):
    pos = []
    peaks = []

    local_max = 0
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i]:
            local_max = i

        if arr[i - 1] <= arr[i] > arr[i + 1] and local_max not in pos and local_max != 0:
            pos.append(local_max)
            peaks.append(arr[local_max])

    return {'pos': pos, 'peaks': peaks}
