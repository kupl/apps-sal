def pick_peaks(arr):
    out = {'pos': [], 'peaks': []}
    if len(arr) == 0:
        return out
    last_i = arr[0]
    latest_maxima = None
    latest_maxima_pos = None
    for pos in range(len(arr)):
        i = arr[pos]
        if i > last_i:
            latest_maxima = i
            latest_maxima_pos = pos
        if i < last_i and latest_maxima is not None:
            out['pos'].append(latest_maxima_pos)
            out['peaks'].append(latest_maxima)
            latest_maxima = None
            latest_maxima_pos = None
        last_i = i
    return out
