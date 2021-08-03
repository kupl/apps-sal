def even_numbers(arr, n):
    return [k for k in arr if k % 2 == 0][-n:]
