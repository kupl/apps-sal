def pick_peaks(arr):
    dict = {'pos': [], 'peaks': []}
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] >= arr[i + 1]:
            add = True
            if arr[i] == arr[i + 1]:
                j = i
                done = False
                while j < len(arr) and add and (not done):
                    if arr[j] > arr[i]:
                        add = False
                    elif arr[j] < arr[i]:
                        done = True
                    j += 1
                if not done:
                    add = False
            if add:
                dict['pos'].append(i)
                dict['peaks'].append(arr[i])
    return dict
