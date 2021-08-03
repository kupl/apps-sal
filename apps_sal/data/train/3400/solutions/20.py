def even_numbers(arr, n):
    return [i for i in arr if i & 1 ^ 1][-n:]
