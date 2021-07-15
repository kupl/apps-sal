def pick_peaks(arr):
    if not arr: 
        return {"pos":[],"peaks":[]}
    else: 
        peak_pos = []
        peak_value = []
        value = 0
        for i in range(1,len(arr)-1):
            if (arr[i-1] < arr[i]) and (arr[i+1] < arr[i]):
                peak_pos.append(i)
                peak_value.append(arr[i])
            if (arr[i-1] < arr[i]) and (arr[i+1] == arr[i]):
                for j in range(i+1,len(arr)):
                    if (arr[j] < arr[i]):
                        peak_pos.append(i)
                        peak_value.append(arr[i])      
                        print(('value added',i,j))
                        break
                    if (arr[j] > arr[i]):
                        break
                    
                        
        return {"pos":peak_pos,"peaks":peak_value}
            

