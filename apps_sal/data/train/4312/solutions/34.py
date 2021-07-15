def pick_peaks(arr):
    peak = []
    pos = []
    prev = 0
    growing = False
    for i in range(1,len(arr)):
        if arr[prev] > arr[i] and growing:
            peak.append(arr[prev])
            pos.append(prev)
            growing = False
        elif arr[prev] < arr[i]:
            growing = True
        if arr[prev] == arr[i]:
            prev = prev
        else:
            prev = i
    return { 'pos' : pos, 'peaks' : peak}

