def pick_peaks(arr):

    print('input:{}'.format(arr))
    if len(arr) < 1:
        return {"pos": [], "peaks": []}

    # your code here
    UP = 0
    DOWN = 1
    FLAT = 2
    trends = ["UP", "DOWN", "FLAT"]

    if arr[0] == arr[1]:
        trend = FLAT
    elif arr[0] > arr[1]:
        trend = DOWN
    else:
        trend = UP

    prev = arr[0]
    pos = []
    peaks = []

    local_max = None
    for i in range(1, len(arr)):
        if trend == UP:
            if arr[i] == prev:
                trend = FLAT
                local_max = i - 1
            elif arr[i] < prev:
                trend = DOWN
                pos.append(i - 1)
                peaks.append(prev)
        elif trend == DOWN:
            if arr[i] == prev:
                trend = FLAT
                local_max = None
            elif arr[i] > prev:
                trend = UP
        elif trend == FLAT:
            if arr[i] > prev:
                trend = UP
            elif arr[i] < prev:
                if local_max != None:
                    pos.append(local_max)
                    peaks.append(prev)
                trend = DOWN

        prev = arr[i]

    # terminated with flat
    if trend == FLAT:
        pos = pos[0:]
        peaks = peaks[0:]
    return {"pos": pos, "peaks": peaks}
