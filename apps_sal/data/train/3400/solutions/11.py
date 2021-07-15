def even_numbers(lst, n):
    return [num for num in lst if not num % 2][-n:]
