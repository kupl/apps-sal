def solve(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] in arr[i + 1:len(arr)]:
            pass
        else:
            result.append(arr[i])
    return result
