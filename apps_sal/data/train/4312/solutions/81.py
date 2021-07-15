def pick_peaks(arr):
    pos = []
    peaker = None
    for i in range(1 ,len(arr)):
        if arr[i-1] < arr[i]:
            peaker = i
        elif arr[i-1] > arr[i] and peaker:
            pos.append(peaker)
            peaker = None
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}
