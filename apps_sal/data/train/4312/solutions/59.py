def pick_peaks(arr):
    #your code here
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif prob_peak and arr[prob_peak] > arr[i]:
            pos.append(prob_peak)
            prob_peak = False
    return {"pos":pos, "peaks":[arr[i] for i in pos]}
