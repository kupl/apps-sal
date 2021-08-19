def pick_peaks(arr):
    dict = {'pos': [], 'peaks': []}
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            dict['pos'].append(i)
            dict['peaks'].append(arr[i])
        elif arr[i - 1] < arr[i] and arr[i] == arr[i + 1]:
            cur = i + 1
            while cur + 1 < len(arr):
                if arr[cur] > arr[cur + 1]:
                    dict['pos'].append(i)
                    dict['peaks'].append(arr[i])
                    break
                if arr[cur] < arr[cur + 1]:
                    break
                cur += 1
    return dict
