def pick_peaks(arr):
    coords = {'pos': [i for i in range(1, len(arr) - 1) if arr[i - 1] < arr[i] >
                    arr[[x for x in range(i, len(arr)) if arr[x] != arr[i] or x == len(arr) - 1][0]]]}
    coords.update({'peaks':[arr[elem] for elem in coords.get('pos') ]})
    return coords
