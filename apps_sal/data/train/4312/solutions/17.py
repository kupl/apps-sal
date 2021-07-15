def pick_peaks(arr):
    pos_delta = [pd for pd in enumerate((b - a for a, b in zip(arr, arr[1:])), 1) if pd[1]]
    positions = [a[0] for a, b in zip(pos_delta, pos_delta[1:]) if a[1] > 0 and b[1] < 0]
    return {'pos': positions, 'peaks': [arr[p] for p in positions]}

