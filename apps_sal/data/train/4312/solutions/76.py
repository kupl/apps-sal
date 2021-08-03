def pick_peaks(arr):
    pos = []
    peaks = []
    if arr:
        cur = arr[0]
        cur_pos = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                cur = arr[i]
                cur_pos = i
            elif arr[i] < cur and cur_pos != 0:
                pos.append(cur_pos)
                peaks.append(cur)
                cur_pos = 0
    return {
        'pos': pos,
        'peaks': peaks
    }
