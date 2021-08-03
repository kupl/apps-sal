def even_numbers(arr, n):
    return [x for x in arr[::-1] if not x % 2][:n][::-1]
