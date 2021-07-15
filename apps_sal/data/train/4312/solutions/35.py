def pick_peaks(arr):
    pos = []
    peaks = []
    for x, num in enumerate(arr):
        if x == 0 or x == len(arr)-1:
            continue
        if arr[x-1] < num and arr[x+1] < num:
            pos.append(x)
            peaks.append(num)
        elif arr[x-1] < num and arr[x+1] == num:
            # checks for plateau peaks
            i = x
            plateau = True
            while plateau:
                i+= 1
                try:
                    if arr[i] < num:
                        pos.append(x)
                        peaks.append(num)
                        plateau = False
                    elif arr[i] > num:
                        plateau = False
                except IndexError:
                    plateau = False
                    
    return {'pos':pos, 'peaks': peaks}
            
            
        

