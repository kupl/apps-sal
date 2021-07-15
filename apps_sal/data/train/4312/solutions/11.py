def pick_peaks(arr):
    redic = { "pos":[], "peaks":[] }
    for i in range(1,len(arr)-1):
        if all(( arr[i] > arr[i-1], arr[i] >= arr[i+1])):
            j = i
            while arr[j] == arr[i] and j < len(arr)-1:
                j += 1
                if arr[j] < arr[i]:
                    redic['pos'].append(i)
                    redic['peaks'].append(arr[i])
    return redic
