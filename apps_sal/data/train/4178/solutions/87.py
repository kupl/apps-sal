def min_sum(arr):
    result = 0
    arr.sort()
    while arr:
        result += arr.pop() * arr.pop(0)
    return result


