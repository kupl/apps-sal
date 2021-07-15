def array_leaders(arr):
    return [arr[x] for x in range(len(arr)) if arr[x] > sum(arr[x + 1:])]
