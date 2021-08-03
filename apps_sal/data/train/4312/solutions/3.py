def pick_peaks(arr):
    peaks = []
    pos = []
    current_pos = None

    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            current_pos = i + 1
        elif arr[i] > arr[i + 1] and i != 0 and current_pos is not None:
            pos += [current_pos]
            peaks += [arr[current_pos]]
            current_pos = None

    return {"pos": pos, "peaks": peaks}
