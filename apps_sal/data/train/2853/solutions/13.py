def solve(arr):
    return [arr[el] for el in range(len(arr)) if arr[el] not in arr[el + 1:]]
