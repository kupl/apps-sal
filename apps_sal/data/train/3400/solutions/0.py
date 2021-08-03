def even_numbers(arr, n):
    return [i for i in arr if i % 2 == 0][-n:]
