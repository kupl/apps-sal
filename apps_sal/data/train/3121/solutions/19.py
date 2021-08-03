def solve(arr):
    result = []
    for i in arr:
        if arr.count(i) != arr.count(-i):
            result.append(i)
    return result[0]
