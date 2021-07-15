def check(arr, n):
    for num in arr:
        if num < n: return True
        elif num > n: return False
    return False
    
def pick_peaks(arr):
    data = {"pos": [], "peaks": []}
    for i, n in enumerate(arr[1:-1], 1):
        if arr[i-1] < n >= arr[i+1] and check(arr[i:], n):
            data["pos"] += [i]
            data["peaks"] += [n]

    return data
