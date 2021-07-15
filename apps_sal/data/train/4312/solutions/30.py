def pick_peaks(arr):
    pos = []
    peaks = []
    i = 1
    while i < len(arr)-1:
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]: #case when there is a simple peak
            pos.append(i); peaks.append(arr[i])
        elif arr[i-1] < arr[i] < arr[i+1]: #case when the value of each number is incrementing
            pass
        elif arr[i-1] < arr[i]: #the case when we have a plato
            if i < len(arr): #to avoid the situation of i value greater then arr len
                for j in range(i,len(arr)-1): #we check all number to len(arr)-1 
                    if arr[j] == arr[j+1]:    #to understand when and where the plato ends
                        continue              #plato continues
                    elif arr[j] < arr[j+1]:   #case when we meet the number which is greater
                        i = j - 1             #then each plato's number
                        break
                    elif arr[j] > arr[j+1]:   #case when the plato has ended we simply add 
                        pos.append(i)         #the i and its value to lists
                        peaks.append(arr[i])
                        i = j - 1
                        break
        i+=1

    return {'pos': pos, 'peaks': peaks}
