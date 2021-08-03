def pick_peaks(arr):
    print(arr)
    peaks = {'pos': [], 'peaks': []}
    enum_arr = list(enumerate(arr))
    possible_peaks = enum_arr[1:-1]
    for point in possible_peaks:
        current_p, current_v = point[0], point[1]
        prior_p, prior_v = enum_arr[current_p - 1]
        next_p, next_v = enum_arr[current_p + 1]
        is_peak = prior_v < current_v > next_v
        if is_peak:
            peaks['pos'].append(current_p)
            peaks['peaks'].append(current_v)
        is_plateau = prior_v == current_v or current_v == next_v
        if is_plateau:
            is_peak = prior_v < current_v
            i = current_p
            while is_peak:
                try:
                    next = enum_arr[i + 1][1]
                    curr = enum_arr[i][1]
                except IndexError:
                    break
                next_plateau = next == curr
                if not next_plateau:
                    peak_end = next < curr
                    if peak_end:
                        peaks['pos'].append(current_p)
                        peaks['peaks'].append(current_v)
                        is_peak = False
                    else:
                        break
                i += 1
    return peaks
