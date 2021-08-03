def isPeak(arr, pos):
    if pos == 0 or pos == len(arr) - 1:
        return False
    if arr[pos - 1] >= arr[pos]:
        return False
    for nextElem in arr[pos + 1:]:
        if nextElem > arr[pos]:
            return False
        if nextElem < arr[pos]:
            return True


def pick_peaks(arr):
    result = {"pos": [], "peaks": []}
    for pos, val in enumerate(arr):
        if isPeak(arr, pos):
            result["pos"].append(pos)
            result["peaks"].append(val)
    return result
