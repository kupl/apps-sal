def even_numbers(arr,n):
    result = []
    for x in reversed(arr):
        if x%2 == 0:
            result.append(x)
            if len(result) == n:
                break
    return list(reversed(result))

