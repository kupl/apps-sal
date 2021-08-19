def solve(arr):
    return [i for (index, i) in enumerate(arr) if i not in arr[index + 1:]]
