def even_numbers(arr,n):
    result = []
    for i in range(len(arr)-1, -1, -1):
        if arr[i] % 2 == 0:
            result.insert(0, arr[i])
            if len(result) == n:
                return result
    return result
