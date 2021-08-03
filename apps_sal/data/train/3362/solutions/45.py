def sum_mix(arr: []):
    result = 0
    for i in arr:
        if isinstance(i, str):
            result += int(i)
        else:
            result += i
    return result
