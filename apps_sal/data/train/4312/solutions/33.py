def pick_peaks(arr):
    peaks = []
    pos = []
    i = 0
    clean = list(arr)
    while i < len(clean) - 1:
        if i == 0 or i == len(clean) - 1:
            i = i + 1
            pass
        else:
            c = 1
            while clean[i] == clean[i + c] and i + c < len(clean) - 1:
                c = c + 1
            if clean[i] > clean[i - 1] and clean[i] > clean[i + c]:
                peaks.append(clean[i])
                pos.append(i)
            i = i + c
    return {'pos': pos, 'peaks': peaks}
