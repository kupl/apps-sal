def pick_peaks(arr):
    dct = {"pos": [], "peaks": []}
    for i in range(1, len(arr) - 1):
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            dct["pos"].append(i)
    plateau_peak(arr, dct)
    dct["pos"].sort()
    dct["peaks"] = [arr[x] for x in dct["pos"]]
    return dct

def plateau_peak(arr, dct):
    last = 0
    for i in range(1, len(arr) - 1):
        if arr[i] == arr[i+1]:
            continue
        elif arr[i] > arr[i+1] and arr[i] == arr[i-1] and arr[i] > arr[last]:
            dct["pos"].append(last+1)
            last = i
        else:
            last = i
