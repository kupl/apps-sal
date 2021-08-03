def first_non_consecutive(arr):
    res = [arr[i] for i in range(1, len(arr)) if arr[i - 1] != arr[i] - 1]
    return res[0] if res else None
