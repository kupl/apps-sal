def SJF(arr, j):
    return sum((k for k in arr if k < arr[j])) + arr[:j + 1].count(arr[j]) * arr[j]
