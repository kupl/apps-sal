def pick_peaks(arr):

    PairList = []

    for i,e in enumerate(arr):
    
        if arr[i-1] >= e or i == 0:
        
            continue
        
        for k in arr[i:]:
        
            if k == e:
            
                continue
                
            elif k > e:
            
                break
                
            else:
            
                PairList.append([i,e])
                break 
    
    return {'pos':[k[0] for k in PairList], 'peaks':[k[1] for k in PairList]}
