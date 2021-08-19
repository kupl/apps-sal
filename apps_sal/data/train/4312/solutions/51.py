def pick_peaks(arr):
    d = {'pos': [], 'peaks': []}
    i = 0
    print(arr)
    if len(arr) > 2 and arr[0] >= arr[1]:
        while arr[i] >= arr[i + 1] and i < len(arr) - 2:
            i += 1
    while i < len(arr) - 1:
        if arr[i] < arr[i + 1]:
            pass
        elif arr[i] == arr[i + 1]:
            temp = i
            while arr[i] == arr[i + 1] and i < len(arr) - 2:
                i += 1
            if arr[i] > arr[i + 1]:
                d['pos'].append(temp)
                d['peaks'].append(arr[temp])
                while arr[i] >= arr[i + 1] and i < len(arr) - 2:
                    i += 1
        else:
            d['pos'].append(i)
            d['peaks'].append(arr[i])
            while arr[i] >= arr[i + 1] and i < len(arr) - 2:
                i += 1
        i += 1
    return d
