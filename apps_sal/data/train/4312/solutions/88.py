def pick_peaks(arr):

    pos=list()
    peaks=list()
    j=0
    
    for i in range(1, len(arr)-1):
        
        if (arr[i-1]<arr[i]) and (arr[i+1]<arr[i]):
            pos.append(i)
            peaks.append(arr[i])

        elif arr[i-1]<arr[i] and arr[i]==arr[i+1] and i+1<len(arr)-1:
            pos.append(i)
            peaks.append(arr[i])
            j=1

        elif j==1 and ((arr[i-1]==arr[i] and arr[i]<arr[i+1]) or \
                       (arr[i]==arr[i+1] and i+1==len(arr)-1)):
            pos.pop()
            peaks.pop()
            j=0

    return {'pos': pos, 'peaks': peaks}

