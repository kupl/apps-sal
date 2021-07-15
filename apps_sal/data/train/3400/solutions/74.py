def even_numbers(arr, n):
    res = [x for x in arr if not x & 1]
    return res[-n:]
