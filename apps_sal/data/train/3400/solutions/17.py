def even_numbers(arr, n):
    return list(filter(lambda x: not x % 2, arr))[-n:]
