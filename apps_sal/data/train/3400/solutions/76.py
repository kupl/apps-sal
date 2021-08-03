def even_numbers(arr, n):
    even_nums = list(filter(lambda x: x % 2 == 0, arr))
    return even_nums[-n:]
