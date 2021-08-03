def pick_peaks(arr):
    setThis = False
    pos = []
    peaks = []
    print([x for x in range(len(arr))])
    print(arr)
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            pos.append(i)
            peaks.append(arr[i])
        elif arr[i] > arr[i - 1] and arr[i] == arr[i + 1]:
            j = i + 1
            while arr[j] == arr[i] and j < len(arr) - 1:
                j += 1
            if j == len(arr) or arr[j] < arr[i]:
                pos.append(i)
                peaks.append(arr[i])
                i = j
    print(pos)
    print(peaks)
    res = {"pos": pos, "peaks": peaks}
    return res
