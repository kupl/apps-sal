def pick_peaks(arr):
    peaks = {"pos":[], "peaks":[]}
    for i in range(1, len(arr)):
        next_num = next((num for num in arr[i:] if num != arr[i]), float("inf"))
        if arr[i-1] < arr[i] and next_num < arr[i]:
            peaks["pos"].append(i)
            peaks["peaks"].append(arr[i])
    return peaks

