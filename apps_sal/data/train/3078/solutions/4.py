def array_center(arr):
    avg = sum(arr) / len(arr)
    return [i for i in arr if abs(i - avg) < min(arr)]
