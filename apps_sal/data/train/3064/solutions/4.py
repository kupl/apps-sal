def transpose(arr):
    if len(arr) == 0:
        return []
    if len(arr[0]) == 0:
        return [[]]
    return [[arr[row][col] for row in range(len(arr))] for col in range(len(arr[0]))]
