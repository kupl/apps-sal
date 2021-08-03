def even_numbers(arr, n):
    result = []
    for num in arr[::-1]:
        if len(result) < n:
            if num % 2 == 0:
                result.append(num)
    return result[::-1]
