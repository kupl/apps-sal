def even_numbers(arr, n):
    return [even_num for even_num in arr if even_num % 2 == 0][-n:]
