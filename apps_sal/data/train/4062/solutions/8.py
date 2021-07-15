def solve(arr):
    result = arr[-1:]
    for x in arr[-1::-1]:
        if x > result[-1]:
            result.append(x)
    return result[::-1]
