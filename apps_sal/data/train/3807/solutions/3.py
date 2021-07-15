def smaller(arr):
    return [sum(j < v for j in arr[i:]) for i, v in enumerate(arr)]
