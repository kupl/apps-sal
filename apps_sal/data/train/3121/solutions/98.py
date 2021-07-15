def solve(arr):
    while len(set(arr)) > 1:
        for i in range(len(arr) - 1):
            if arr.count(-arr[i]):
                arr.remove(-arr[i])
                arr.remove(arr[i])
                break
    return (list(set(arr))[0])
