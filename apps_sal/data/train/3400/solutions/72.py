def even_numbers(arr, length):
    return [n for n in arr if n % 2 == 0][-length:]
