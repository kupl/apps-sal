def smaller(arr):
    return [sum((x > y for y in arr[i + 1:])) for (i, x) in enumerate(arr)]
