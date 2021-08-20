def pick_peaks(arr):
    pos = []
    peaks = []
    for x in range(len(arr)):
        if x != 0 and x != len(arr) - 1:
            if arr[x] > arr[x - 1] and arr[x] > arr[x + 1]:
                pos.append(x)
                peaks.append(arr[x])
            elif arr[x] > arr[x - 1] and arr[x] >= arr[x + 1]:
                for y in arr[x:]:
                    print((y, x, arr[x], arr[x:]))
                    if arr[x] > y:
                        pos.append(x)
                        peaks.append(arr[x])
                        break
                    elif arr[x] < y:
                        break
    return {'pos': pos, 'peaks': peaks}
