def pick_peaks(arr):
    res = {'pos': [], 'peaks': []}
    flag = False
    for i in range(1, len(arr) - 1):
        if flag:
            if arr[i] == arr[i + 1]:
                continue
            elif arr[i] > arr[i + 1]:
                res['pos'].append(temp)
                res['peaks'].append(arr[i])
                flag = False
            else:
                flag = False
        elif arr[i] > arr[i - 1]:
            if arr[i] > arr[i + 1]:
                res['pos'].append(i)
                res['peaks'].append(arr[i])
            elif arr[i] == arr[i + 1]:
                temp = i
                flag = True
    return res
