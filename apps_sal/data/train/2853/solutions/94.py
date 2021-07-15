def solve(arr): 
    result = []
    arr = arr[::-1]
    for i in arr:
        if i not in result:
            result.append(i)
    return result[::-1]
