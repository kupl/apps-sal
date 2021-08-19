def pick_peaks(arr):
    if not arr:
        return {'pos': [], 'peaks': []}
    pos = []
    peaks = []
    arr_iter = enumerate(arr)
    (curr_pos, curr_peak) = next(arr_iter)
    climbing = False
    for (index, value) in arr_iter:
        if value > curr_peak:
            (curr_pos, curr_peak) = (index, value)
            climbing = True
        elif value < curr_peak:
            if climbing:
                pos.append(curr_pos)
                peaks.append(curr_peak)
                climbing = False
            (curr_pos, curr_peak) = (index, value)
    return {'pos': pos, 'peaks': peaks}
