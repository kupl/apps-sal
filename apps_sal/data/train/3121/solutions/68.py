def solve(arr):
    for idx, num in enumerate(arr):
        if num in (arr[:idx] + arr[idx+1:]):
            return arr[idx]
    return sum(arr)

