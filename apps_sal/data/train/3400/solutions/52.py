def even_numbers(arr, n):
    x = -1
    result = []
    while n > 0:
        if arr[x] % 2 == 0:
            result.append(arr[x])
            n -= 1
            x -= 1
        else:
            x -= 1
    return list(reversed(result))
