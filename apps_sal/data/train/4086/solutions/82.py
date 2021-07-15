def first_non_consecutive(arr):
    i = 0
    while i < len(arr) - 1:
        i += 1
        if arr[0] >= 0 and arr[i] - arr[i - 1] != 1:
            return arr[i]
            break
        elif arr[0] < 0 and abs(arr[i - 1]) - abs(arr[i]) != 1:
            return arr[i]
            break
    else:
        return None
