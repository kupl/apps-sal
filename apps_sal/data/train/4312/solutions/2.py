def pick_peaks(arr):
    
    def add_peak(p):
        peaks["pos"].append(p)
        peaks["peaks"].append(arr[p])
        
    def is_peak(p):
        return arr[p-1] < arr[p] > arr[p+1]
        
    def is_plateau_start(p):
        return arr[p-1] < arr[p] == arr[p+1]
        
    def does_plateau_end_lower(p):
        return next((val for val in arr[p+1:] if val != arr[p]), arr[p]) < arr[p]

    peaks = {"pos":[], "peaks":[]}
    for p in range(1, len(arr)-1):
        if is_peak(p):
            add_peak(p)
        elif is_plateau_start(p) and does_plateau_end_lower(p):
            add_peak(p)
    
    return peaks
