def even_numbers(arr, n):
    s = [num for num in arr if num % 2 == 0]
    return s[-n:]
