def even_numbers(arr, n):
    return [i for i in arr if not i % 2][-n:]
