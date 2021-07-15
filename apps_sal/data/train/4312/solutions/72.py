def pick_peaks(arr):
    set = {'pos' : [], 'peaks' : []}
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            set['pos'].append(i)
            set['peaks'].append(arr[i])
        if arr[i] == arr[i+1] and arr[i] > arr[i-1]:
            for x in range(i+2, len(arr)):
                if arr[i]<arr[x]:
                    break
                if arr[i]>arr[x]:
                    set['pos'].append(i)
                    set['peaks'].append(arr[i])
                    break
    return set
