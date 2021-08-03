def pick_peaks(arr):
    out = {}
    pos = []
    peaks = []
    temp = []
    for i, x in enumerate(arr[1:-1], start=1):
        prev = arr[i - 1]
        nxt = arr[i + 1]
        if x > prev:
            temp = [i, x]
        if x < prev and temp or x > nxt and temp:
            pos.append(temp[0])
            peaks.append(temp[1])
            temp.clear()

    out['pos'] = pos
    out['peaks'] = peaks
    return out
