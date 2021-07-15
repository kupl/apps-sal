def even_numbers(arr, num):
    return [n for n in arr if n % 2 == 0][-num:]
