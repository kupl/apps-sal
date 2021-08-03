def even_numbers(arr, n):
    return [even for even in arr if even % 2 == 0][-n:]
