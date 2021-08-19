def pick_peaks(arr):
    pos = []
    peaks = []
    if len(arr) > 0:
        n = 0
        peak_start = 0
        curr_height = arr[0]
        is_descending = True
        for p in arr:
            if p > curr_height:
                is_descending = False
                curr_height = p
                peak_start = n
            elif p == curr_height:
                pass
            elif p < curr_height:
                if not is_descending:
                    pos.append(peak_start)
                    peaks.append(curr_height)
                is_descending = True
                curr_height = p
            else:
                raise Error
            n += 1
    return {'pos': pos, 'peaks': peaks}
