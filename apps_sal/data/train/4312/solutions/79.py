def pick_peaks(a):
    previous = 0
    current = 0
    pos = []
    peaks = []
    for next in range(1, len(a)):
        if a[next] > a[current]:
            previous = current
            current = next
        elif a[next] < a[current]:
            if a[previous] < a[current]:
                pos.append(current)
                peaks.append(a[current])
            previous = current
            current = next
    return {'pos': pos, 'peaks': peaks}
