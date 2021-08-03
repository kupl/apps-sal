def pick_peaks(arr):
    r = {'pos': [], 'peaks': []}
    state = 'none'
    c = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            state = 'up'
        elif arr[i] == arr[i - 1]:
            if state == 'still':
                c += 1
            if state == 'up':
                state = 'still'
        elif arr[i] < arr[i - 1]:
            if state == 'up':
                r['pos'].append(i - 1)
                r['peaks'].append(arr[i - 1])
            elif state == 'still':
                r['pos'].append(i - c - 1)
                r['peaks'].append(arr[i - c - 1])
            state = 'down'
    return r
