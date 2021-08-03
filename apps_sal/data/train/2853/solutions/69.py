def solve(arr):
    result = []
    for i in range(len(arr)):
        try:
            if arr[i] not in arr[i + 1:]:
                result.append(arr[i])
        except IndexError:
            pass
    return result
